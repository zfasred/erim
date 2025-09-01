# carbon/urls.py
from django.urls import path
from . import views

app_name = 'carbon'

urlpatterns = [
    # Dashboard
    path('', views.dashboard_view, name='dashboard'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Yönetim (Emisyon Faktörleri, Yakıt Türleri)
    path('management/', views.management_list_view, name='management-list'),
    
    # Emisyon Faktörleri
    path('emissionfactor/create/', views.emissionfactor_create_view, name='emissionfactor-create'),
    path('emissionfactor/<int:pk>/update/', views.emissionfactor_update_view, name='emissionfactor-update'),
    path('emissionfactor/<int:pk>/delete/', views.emissionfactor_delete_view, name='emissionfactor-delete'),
    
    # Yakıt Türleri
    path('fueltype/create/', views.fueltype_create_view, name='fueltype-create'),
    path('fueltype/<int:pk>/update/', views.fueltype_update_view, name='fueltype-update'),
    path('fueltype/<int:pk>/delete/', views.fueltype_delete_view, name='fueltype-delete'),
    
    # KAPSAM 1 - Doğrudan Emisyonlar
    path('scope1/', views.scope1_list_view, name='scope1-list'),
    path('scope1/create/', views.scope1_create_view, name='scope1-create'),
    path('scope1/<int:pk>/update/', views.scope1_update_view, name='scope1-update'),
    path('scope1/<int:pk>/delete/', views.scope1_delete_view, name='scope1-delete'),
    
    # KAPSAM 2 - Elektrik
    path('scope2/', views.scope2_list_view, name='scope2-list'),
    path('scope2/create/', views.scope2_create_view, name='scope2-create'),
    path('scope2/<int:pk>/update/', views.scope2_update_view, name='scope2-update'),
    path('scope2/<int:pk>/delete/', views.scope2_delete_view, name='scope2-delete'),
    
    # KAPSAM 3 - Ulaşım
    path('scope3/', views.scope3_list_view, name='scope3-list'),
    path('scope3/create/', views.scope3_create_view, name='scope3-create'),
    path('scope3/<int:pk>/update/', views.scope3_update_view, name='scope3-update'),
    path('scope3/<int:pk>/delete/', views.scope3_delete_view, name='scope3-delete'),
    
    # KAPSAM 4 - Satın Alınan Ürünler
    path('scope4/', views.scope4_list_view, name='scope4-list'),
    path('scope4/create/', views.scope4_create_view, name='scope4-create'),
    path('scope4/<int:pk>/update/', views.scope4_update_view, name='scope4-update'),
    path('scope4/<int:pk>/delete/', views.scope4_delete_view, name='scope4-delete'),
    
    # Toplu İşlemler
    path('bulk-upload/', views.bulk_upload_view, name='bulk-upload'),
    path('bulk-upload/template/<str:scope>/', views.download_template_view, name='download-template'),
    
    # Raporlar
    path('report/', views.report_list_view, name='report-list'),
    path('report/generate/', views.report_generate_view, name='report-generate'),
    path('report/<int:pk>/detail/', views.report_detail_view, name='report-detail'),
    path('report/<int:pk>/download/', views.report_download_view, name='report-download'),
    
    # API Endpoints (AJAX için)
    path('api/calculate-emission/', views.api_calculate_emission, name='api-calculate-emission'),
    path('api/get-fuel-factors/<int:fuel_id>/', views.api_get_fuel_factors, name='api-get-fuel-factors'),
    path('api/chart-data/', views.api_chart_data, name='api-chart-data'),
    
    # Eski URL'ler (backward compatibility)
    path('input/', views.input_list_view, name='input-list'),
    path('inputdata/create/', views.inputdata_create_view, name='inputdata-create'),
    path('inputdata/<int:pk>/update/', views.inputdata_update_view, name='inputdata-update'),
    path('inputdata/<int:pk>/delete/', views.inputdata_delete_view, name='inputdata-delete'),
]