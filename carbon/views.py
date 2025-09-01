from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from .models import CoefficientType, EmissionFactor, InputCategory, InputData, Report, Firm
from .forms import CoefficientTypeForm, EmissionFactorForm, InputCategoryForm, InputDataForm, ReportForm, UserFirmAccessForm

from core.models import UserFirm

@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def management_list_view(request):
    factors = EmissionFactor.objects.all()
    types = CoefficientType.objects.all()
    context = {'factors': factors, 'types': types}

    if request.user.has_perm('carbon.can_manage_user_firm_access'):
        if request.method == 'POST':
            form = UserFirmAccessForm(request.POST)
            if form.is_valid():
                selected_user = form.cleaned_data['user']
                selected_firm = form.cleaned_data['firm']
                try:
                    # Check if the association already exists
                    UserFirm.objects.get(user=selected_user, firm=selected_firm)
                except UserFirm.DoesNotExist:
                    # Create new association with 'create' field set
                    UserFirm.objects.create(user=selected_user, firm=selected_firm, create=timezone.now())

                from django.contrib import messages
                messages.success(request, f"'{selected_user.username}' kullanıcısı '{selected_firm.name}' firmasına başarıyla atandı.")
                return redirect('carbon:management-list')

        else:
            form = UserFirmAccessForm()
        context['user_firm_form'] = form

    return render(request, 'carbon/management_list.html', context)

@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def emissionfactor_create_view(request):
    if request.method == 'POST':
        form = EmissionFactorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carbon:management-list')
    else:
        form = EmissionFactorForm()
    return render(request, 'carbon/emissionfactor_form.html', {'form': form})

@login_required
@permission_required('carbon.change_emissionfactor', raise_exception=True)
def emissionfactor_update_view(request, pk):
    factor = get_object_or_404(EmissionFactor, pk=pk)
    if request.method == 'POST':
        form = EmissionFactorForm(request.POST, instance=factor)
        if form.is_valid():
            form.save()
            return redirect('carbon:management-list')
    else:
        form = EmissionFactorForm(instance=factor)
    return render(request, 'carbon/emissionfactor_form.html', {'form': form})

@login_required
@permission_required('carbon.delete_emissionfactor', raise_exception=True)
def emissionfactor_delete_view(request, pk):
    factor = get_object_or_404(EmissionFactor, pk=pk)
    if request.method == 'POST':
        factor.delete()
        return redirect('carbon:management-list')
    return render(request, 'carbon/emissionfactor_confirm_delete.html', {'factor': factor})

@permission_required('carbon.view_input_carbon', raise_exception=True)
def input_list_view(request):
    # Bu view'ın hangi firmanın verilerini göstereceğini bilmesi gerekiyor.
    # Şimdilik örnek olarak ilk firmayı alalım.
    # Daha sonra burayı, kullanıcının seçtiği bir firmayı alacak şekilde güncelleyeceğiz.
    firm = Firm.objects.first() 
    if firm:
        inputs = InputData.objects.filter(firm=firm)
    else:
        inputs = InputData.objects.none()

    context = {'inputs': inputs, 'firm': firm}
    return render(request, 'carbon/input_list.html', context)

@login_required
@permission_required('carbon.add_inputdata', raise_exception=True)
def inputdata_create_view(request):
    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            input_data = form.save(commit=False)
            if hasattr(request.user, 'user'):
                firm = Firm.objects.filter(userfirm__user=request.user.user).first()
                if not firm:
                    raise PermissionDenied("No associated firm found.")
                input_data.firm = firm
            input_data.created_by = request.user.user if hasattr(request.user, 'user') else None
            input_data.save()
            return redirect('carbon:input-list')
    else:
        form = InputDataForm()
    return render(request, 'carbon/inputdata_form.html', {'form': form})

@login_required
@permission_required('carbon.change_inputdata', raise_exception=True)
def inputdata_update_view(request, pk):
    input_data = get_object_or_404(InputData, pk=pk)
    if hasattr(request.user, 'user') and input_data.firm not in Firm.objects.filter(userfirm__user=request.user.user):
        raise PermissionDenied
    if request.method == 'POST':
        form = InputDataForm(request.POST, instance=input_data)
        if form.is_valid():
            form.save()
            return redirect('carbon:input-list')
    else:
        form = InputDataForm(instance=input_data)
    return render(request, 'carbon/inputdata_form.html', {'form': form})

@login_required
@permission_required('carbon.delete_inputdata', raise_exception=True)
def inputdata_delete_view(request, pk):
    input_data = get_object_or_404(InputData, pk=pk)
    if hasattr(request.user, 'user') and input_data.firm not in Firm.objects.filter(userfirm__user=request.user.user):
        raise PermissionDenied
    if request.method == 'POST':
        input_data.delete()
        return redirect('carbon:input-list')
    return render(request, 'carbon/inputdata_confirm_delete.html', {'input_data': input_data})

@login_required
@permission_required('carbon.view_report_carbon', raise_exception=True)
def report_list_view(request):
    if hasattr(request.user, 'user'):
        user_firms = Firm.objects.filter(user_associations__user=request.user.user)
    else:
        user_firms = Firm.objects.none()
    reports = Report.objects.filter(firm__in=user_firms)
    context = {'reports': reports}
    return render(request, 'carbon/report_list.html', context)

@login_required
@permission_required('carbon.add_report', raise_exception=True)
def report_generate_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report_date = form.cleaned_data['report_date']
            if hasattr(request.user, 'user'):
                firm = Firm.objects.filter(userfirm__user=request.user.user).first()
                if not firm:
                    raise PermissionDenied("No associated firm found.")
            else:
                raise PermissionDenied("User profile not found.")

            inputs = InputData.objects.filter(firm=firm, period_end__lte=report_date)

            total_co2e = 0.0
            direct_emissions = 0.0
            indirect_emissions = 0.0
            details = {}

            for input_data in inputs:
                factor = EmissionFactor.objects.filter(
                    Q(category=input_data.category.scope),
                    Q(valid_from__lte=report_date),
                    Q(valid_to__gte=report_date) | Q(valid_to__isnull=True)
                ).order_by('-valid_from').first()

                if factor:
                    co2e = input_data.value * factor.value  # Adapt to full formula as needed
                    total_co2e += co2e
                    if input_data.category.scope in ['KAPSAM_1', 'KAPSAM_2']:
                        direct_emissions += co2e
                    else:
                        indirect_emissions += co2e
                    details[input_data.id] = {
                        'input_value': input_data.value,
                        'factor_value': factor.value,
                        'calculated_co2e': co2e
                    }

            direct_ratio = (direct_emissions / total_co2e * 100) if total_co2e > 0 else 0.0
            indirect_ratio = (indirect_emissions / total_co2e * 100) if total_co2e > 0 else 0.0

            report = Report.objects.create(
                firm=firm,
                report_date=report_date,
                total_co2e=total_co2e,
                direct_ratio=direct_ratio,
                indirect_ratio=indirect_ratio,
                json_details=details,
                generated_by=request.user.user if hasattr(request.user, 'user') else None
            )
            return redirect('carbon:report-list')
    else:
        form = ReportForm(initial={'report_date': datetime.date.today()})
    return render(request, 'carbon/report_form.html', {'form': form})

@login_required
@permission_required('carbon.view_report_carbon', raise_exception=True)
def report_detail_view(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if hasattr(request.user, 'user') and report.firm not in Firm.objects.filter(userfirm__user=request.user.user):
        raise PermissionDenied
    context = {'report': report}
    return render(request, 'carbon/report_detail.html', context)

@login_required
@permission_required('carbon.view_inputdata', raise_exception=True)
def input_list_view(request):
    # Kullanıcının ilişkili olduğu firmaları bul
    user_profile = request.user.user
    user_firms = Firm.objects.filter(user_associations__user=user_profile)

    # Eğer kullanıcının sadece bir firması varsa, onu otomatik seç
    selected_firm = user_firms.first()

    # Eğer formdan bir firma seçimi geldiyse, onu kullan
    firm_pk = request.GET.get('firm_pk')
    if firm_pk:
        selected_firm = get_object_or_404(Firm, pk=firm_pk)

    inputs = InputData.objects.none() # Başlangıçta boş liste
    if selected_firm:
        inputs = InputData.objects.filter(firm=selected_firm)

    context = {
        'inputs': inputs,
        'user_firms': user_firms,
        'selected_firm': selected_firm
    }
    return render(request, 'carbon/input_list.html', context)


@login_required
@permission_required('carbon.add_inputdata', raise_exception=True)
def inputdata_create_view(request):
    firm_pk = request.GET.get('firm_pk') # Hangi firma için eklendiğini al
    firm = get_object_or_404(Firm, pk=firm_pk)

    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            input_data = form.save(commit=False)
            input_data.firm = firm # Girdiyi firmaya bağla
            input_data.save()
            return redirect('carbon:input-list')
    else:
        form = InputDataForm()

    return render(request, 'carbon/inputdata_form.html', {'form': form, 'firm': firm})