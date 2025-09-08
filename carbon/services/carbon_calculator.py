# services/carbon_calculator.py
"""Karbon Ayak İzi Hesaplama Servisleri"""

from decimal import Decimal
from datetime import date, datetime
from typing import Dict, List, Optional
from django.db import transaction
from django.db.models import Sum, Q

from ..models import (
    EmissionFactor, CompanyCarbonReport, 
    Scope1Emission, Scope2Emission, Scope3Emission, Scope4Emission,
    ProductCarbonAllocation, GWPValue
)


class CarbonCalculatorService:
    """Ana karbon hesaplama servisi"""
    
    def __init__(self, company, year, month=None):
        self.company = company
        self.year = year
        self.month = month
        self.report = None
        
        # GWP değerlerini yükle
        self.gwp_values = self._load_gwp_values()
    
    def _load_gwp_values(self):
        """Güncel GWP değerlerini yükle"""
        today = date.today()
        values = {}
        
        gwp_ch4 = GWPValue.objects.filter(
            gas_name='CH4',
            valid_from__lte=today,
            Q(valid_to__gte=today) | Q(valid_to__isnull=True)
        ).first()
        
        gwp_n2o = GWPValue.objects.filter(
            gas_name='N2O',
            valid_from__lte=today,
            Q(valid_to__gte=today) | Q(valid_to__isnull=True)
        ).first()
        
        values['CH4'] = gwp_ch4.gwp_value if gwp_ch4 else Decimal('27.9')
        values['N2O'] = gwp_n2o.gwp_value if gwp_n2o else Decimal('273')
        
        return values
    
    def get_emission_factor(self, name: str, factor_type: str, calculation_date: date = None) -> EmissionFactor:
        """Belirli bir tarih için geçerli emisyon faktörünü getir"""
        if calculation_date is None:
            calculation_date = date.today()
        
        factor = EmissionFactor.objects.filter(
            name=name,
            factor_type=factor_type,
            valid_from__lte=calculation_date,
            Q(valid_to__gte=calculation_date) | Q(valid_to__isnull=True)
        ).first()
        
        if not factor:
            raise ValueError(f"Emisyon faktörü bulunamadı: {name} ({factor_type})")
        
        return factor
    
    @transaction.atomic
    def create_or_update_report(self) -> CompanyCarbonReport:
        """Rapor oluştur veya güncelle"""
        
        # Dönem tarihlerini belirle
        if self.month:
            start_date = date(self.year, self.month, 1)
            if self.month == 12:
                end_date = date(self.year, 12, 31)
            else:
                end_date = date(self.year, self.month + 1, 1) - timedelta(days=1)
        else:
            start_date = date(self.year, 1, 1)
            end_date = date(self.year, 12, 31)
        
        # Rapor oluştur veya getir
        self.report, created = CompanyCarbonReport.objects.update_or_create(
            company=self.company,
            report_year=self.year,
            report_month=self.month,
            defaults={
                'start_date': start_date,
                'end_date': end_date,
                'status': 'DRAFT'
            }
        )
        
        return self.report
    
    def calculate_scope1(self, emissions_data: List[Dict]) -> Decimal:
        """Kapsam 1 emisyonlarını hesapla
        
        emissions_data örnek format:
        [
            {
                'emission_type': 'STATIONARY',
                'fuel_name': 'DOĞALGAZ',
                'consumption_value': 9196678,
                'consumption_unit': 'm3',
                'factor_name': 'Doğalgaz'
            },
            {
                'emission_type': 'MOBILE',
                'fuel_name': 'Motorin',
                'consumption_value': 15000,
                'consumption_unit': 'litre',
                'factor_name': 'Motorin'
            }
        ]
        """
        
        total_co2e = Decimal('0')
        
        # Mevcut kayıtları temizle
        self.report.scope1_emissions.all().delete()
        
        for data in emissions_data:
            # Emisyon faktörünü getir
            factor = self.get_emission_factor(
                data['factor_name'], 
                'FUEL',
                self.report.start_date
            )
            
            # Emisyon kaydı oluştur
            emission = Scope1Emission.objects.create(
                report=self.report,
                emission_type=data['emission_type'],
                fuel_name=data['fuel_name'],
                consumption_value=Decimal(str(data['consumption_value'])),
                consumption_unit=data['consumption_unit'],
                emission_factor=factor,
                gwp_ch4=self.gwp_values['CH4'],
                gwp_n2o=self.gwp_values['N2O']
            )
            
            total_co2e += emission.co2e_total
        
        # Raporu güncelle
        self.report.scope1_total = total_co2e
        self.report.save()
        
        return total_co2e
    
    def calculate_scope2(self, electricity_data: List[Dict]) -> Decimal:
        """Kapsam 2 emisyonlarını hesapla
        
        electricity_data örnek format:
        [
            {
                'facility_name': 'ASANSÖR D2',
                'electricity_kwh': 7955030
            },
            {
                'facility_name': 'DÖKÜMHANE D3',
                'electricity_kwh': 7118068
            }
        ]
        """
        
        total_co2e = Decimal('0')
        
        # Mevcut kayıtları temizle
        self.report.scope2_emissions.all().delete()
        
        # Türkiye elektrik şebekesi emisyon faktörünü getir
        factor = self.get_emission_factor(
            'Türkiye Elektrik Şebekesi',
            'ELECTRICITY',
            self.report.start_date
        )
        
        for data in electricity_data:
            emission = Scope2Emission.objects.create(
                report=self.report,
                facility_name=data['facility_name'],
                electricity_kwh=Decimal(str(data['electricity_kwh'])),
                emission_factor=factor
            )
            
            total_co2e += emission.co2e_total
        
        # Raporu güncelle
        self.report.scope2_total = total_co2e
        self.report.save()
        
        return total_co2e
    
    def calculate_scope3(self, transport_data: List[Dict]) -> Decimal:
        """Kapsam 3 emisyonlarını hesapla"""
        
        total_co2e = Decimal('0')
        
        # Mevcut kayıtları temizle
        self.report.scope3_emissions.all().delete()
        
        for data in transport_data:
            factor = self.get_emission_factor(
                data['factor_name'],
                'TRANSPORT',
                self.report.start_date
            )
            
            # Basit hesaplama - detaylar eklenebilir
            if data.get('fuel_consumption'):
                # Yakıt bazlı hesaplama
                co2e = self._calculate_fuel_emission(
                    data['fuel_consumption'],
                    factor
                )
            elif data.get('distance_km'):
                # Mesafe bazlı hesaplama
                co2e = self._calculate_distance_emission(
                    data['distance_km'],
                    factor,
                    data.get('vehicle_type')
                )
            else:
                co2e = Decimal('0')
            
            emission = Scope3Emission.objects.create(
                report=self.report,
                transport_type=data['transport_type'],
                description=data.get('description', ''),
                fuel_consumption=data.get('fuel_consumption'),
                distance_km=data.get('distance_km'),
                vehicle_type=data.get('vehicle_type', ''),
                emission_factor=factor,
                co2e_total=co2e
            )
            
            total_co2e += co2e
        
        self.report.scope3_total = total_co2e
        self.report.save()
        
        return total_co2e
    
    def calculate_scope4(self, materials_data: List[Dict]) -> Decimal:
        """Kapsam 4 emisyonlarını hesapla
        
        materials_data örnek format:
        [
            {
                'material_name': 'SİLİSLİ SAC',
                'quantity_kg': 810000,
                'factor_name': 'Çelik'
            },
            {
                'material_name': 'PİK DÖKÜM',
                'quantity_kg': 439000,
                'factor_name': 'Dökme Demir'
            }
        ]
        """
        
        total_co2e = Decimal('0')
        
        # Mevcut kayıtları temizle
        self.report.scope4_emissions.all().delete()
        
        for data in materials_data:
            factor = self.get_emission_factor(
                data['factor_name'],
                'MATERIAL',
                self.report.start_date
            )
            
            emission = Scope4Emission.objects.create(
                report=self.report,
                material_name=data['material_name'],
                quantity_kg=Decimal(str(data['quantity_kg'])),
                emission_factor=factor
            )
            
            total_co2e += emission.co2e_total
        
        self.report.scope4_total = total_co2e
        self.report.save()
        
        return total_co2e
    
    def allocate_to_products(self, products_data: List[Dict]):
        """Karbon emisyonunu ürünlere dağıt
        
        products_data örnek format:
        [
            {
                'product_name': 'ASANSÖR MOTORU',
                'annual_production': 60860,
                'annual_weight_kg': 21301000
            },
            {
                'product_name': 'KASNAK',
                'annual_production': 41184,
                'annual_weight_kg': 2059200
            }
        ]
        """
        
        # Toplam ağırlık ve emisyonu hesapla
        total_weight = sum(Decimal(str(p['annual_weight_kg'])) for p in products_data)
        total_emission = self.report.calculate_total()
        
        # Mevcut dağılımları temizle
        self.report.product_allocations.all().delete()
        
        for product in products_data:
            allocation = ProductCarbonAllocation(
                report=self.report,
                product_name=product['product_name'],
                annual_production=product['annual_production'],
                annual_weight_kg=Decimal(str(product['annual_weight_kg']))
            )
            
            allocation.calculate_allocation(total_weight, total_emission)
            allocation.save()
    
    def generate_full_report(self, all_data: Dict) -> Dict:
        """Tam kapsamlı rapor oluştur"""
        
        # Rapor oluştur
        self.create_or_update_report()
        
        # Her kapsam için hesapla
        results = {
            'company': self.company.name,
            'year': self.year,
            'month': self.month,
            'scopes': {}
        }
        
        if 'scope1' in all_data:
            results['scopes']['scope1'] = {
                'total': self.calculate_scope1(all_data['scope1']),
                'details': list(self.report.scope1_emissions.values())
            }
        
        if 'scope2' in all_data:
            results['scopes']['scope2'] = {
                'total': self.calculate_scope2(all_data['scope2']),
                'details': list(self.report.scope2_emissions.values())
            }
        
        if 'scope3' in all_data:
            results['scopes']['scope3'] = {
                'total': self.calculate_scope3(all_data['scope3']),
                'details': list(self.report.scope3_emissions.values())
            }
        
        if 'scope4' in all_data:
            results['scopes']['scope4'] = {
                'total': self.calculate_scope4(all_data['scope4']),
                'details': list(self.report.scope4_emissions.values())
            }
        
        # Ürün dağılımı
        if 'products' in all_data:
            self.allocate_to_products(all_data['products'])
            results['product_allocations'] = list(
                self.report.product_allocations.values()
            )
        
        # Toplam emisyon
        results['total_emission'] = self.report.calculate_total()
        
        # Rapor durumunu güncelle
        self.report.status = 'COMPLETED'
        self.report.save()
        
        return results
    
    def _calculate_fuel_emission(self, fuel_liters: Decimal, factor: EmissionFactor) -> Decimal:
        """Yakıt bazlı emisyon hesapla"""
        # Excel formülüne benzer hesaplama
        if factor.nkd and factor.density:
            co2 = fuel_liters * factor.co2_factor * factor.nkd * factor.density * Decimal('0.000000001')
            ch4 = fuel_liters * factor.ch4_factor * factor.nkd * factor.density * Decimal('0.000000001')
            n2o = fuel_liters * factor.n2o_factor * factor.nkd * factor.density * Decimal('0.000000001')
            
            co2e = co2 + (ch4 * self.gwp_values['CH4']) + (n2o * self.gwp_values['N2O'])
            return co2e
        
        return Decimal('0')
    
    def _calculate_distance_emission(self, distance_km: Decimal, factor: EmissionFactor, 
                                    vehicle_type: str = None) -> Decimal:
        """Mesafe bazlı emisyon hesapla"""
        # Basit hesaplama - detaylandırılabilir
        return distance_km * factor.co2_factor / 1000