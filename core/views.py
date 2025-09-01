from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.db.models import Q
from .models import Firm, District, Personnel, Department, Education, Blood, User, UserGroup, Language, Media
from .forms import FirmForm, FirmSoftDeleteForm, PersonnelForm, DepartmentForm, UserProfileForm


@login_required
def portal_view(request):
    # Projedeki tüm modüllerin bir listesini tanımlıyoruz.
    # Gelecekte yeni modül eklediğimizde, onu sadece bu listeye ekleyeceğiz.
    all_modules = [
        {
            'name': 'Firma Yönetimi',
            'url_name': 'core:firm-list', # URL'in adı
            'icon': '🏢', # Kutucuk için ikon
            'permission': 'core.view_firm', # Bu modülü görmek için gereken izin
        },
        # Personel modülü doğrudan firmalar üzerinden yönetildiği için,
        # ana modül linki yine firma listesine gidebilir.
        {
            'name': 'Personel Yönetimi',
            'url_name': 'core:firm-list',
            'icon': '👥',
            'permission': 'core.view_personnel',
        },
        {
            'name': 'Genel Yönetim (Admin)',
            'url': '/admin/', # Bu özel bir URL olduğu için adını değil, direkt yolunu yazıyoruz
            'icon': '⚙️',
            'permission': 'is_staff', # Bu da özel bir yetki kontrolü
        },
        {
            'name': 'Kullanıcı Yönetimi',
            'url_name': 'core:user-list',
            'icon': '👤',
            'permission': 'core.view_user',
        },
        {
            'name': 'Karbon Yönetim',
            'url_name': 'carbon:management-list',
            'icon': '🌍',
            'permission': 'carbon.view_management_carbon',
        },
        {
            'name': 'Karbon Girdi',
            'url_name': 'carbon:input-list',
            'icon': '📝',
            'permission': 'carbon.view_input_carbon',
        },
        {
            'name': 'Karbon Rapor',
            'url_name': 'carbon:report-list',
            'icon': '📊',
            'permission': 'carbon.view_report_carbon',
        },
    ]

    # Kullanıcının görebileceği modüller için boş bir liste oluşturuyoruz.
    allowed_modules = []
    for module in all_modules:
        permission_name = module.get('permission')

        # Django'nun standart yetki kontrolünü kullanıyoruz
        # 'is_staff' özel bir durum, admin paneli için
        if permission_name == 'is_staff' and request.user.is_staff:
            allowed_modules.append(module)
        # Diğer tüm izinler için has_perm metodu
        elif request.user.has_perm(permission_name):
            allowed_modules.append(module)

    context = {
        'modules': allowed_modules
    }
    return render(request, 'portal.html', context)


@permission_required('core.view_firm', raise_exception=True)
def firm_list_view(request):
    # Arama kutusundan gelen 'q' parametresini al
    query = request.GET.get('q')

    show_deleted = request.GET.get('show_deleted')

    if show_deleted:
        base_queryset = Firm.objects.filter(delete__isnull=False)
        list_title = "Silinmiş Firmalar"
    else:
        base_queryset = Firm.objects.filter(delete__isnull=True)
        list_title = "Aktif Firmalar"

    # Eğer bir arama sorgusu varsa, listeyi filtrele
    if query:
        # name, city__name (ilişkili modelin alanı) veya tax alanlarından
        # HERHANGİ BİRİ arama terimini içeriyorsa...
        base_queryset = base_queryset.filter(
            Q(name__icontains=query) |
            Q(city__name__icontains=query) |
            Q(tax__icontains=query)
        )
        list_title += f" (Arama Sonuçları: '{query}')"

    context = {
        'firms': base_queryset,
        'list_title': list_title,
        'is_showing_deleted': bool(show_deleted)
    }
    return render(request, 'firm_list.html', context)

@permission_required('core.add_firm', raise_exception=True)
def firm_create_view(request):
    form = FirmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('core:firm-list')
    return render(request, 'firm_form.html', {'form': form})

@permission_required('core.change_firm', raise_exception=True)
def firm_update_view(request, pk):
    firm = get_object_or_404(Firm, pk=pk)
    form = FirmForm(request.POST or None, request.FILES or None, instance=firm)
    if form.is_valid():
        instance = form.save(commit=False)

        if 'delete' in form.cleaned_data:
            instance.delete = form.cleaned_data['delete']

        instance.save()

        return redirect('core:firm-list')
    return render(request, 'firm_form.html', {'form': form})

@permission_required('core.delete_firm', raise_exception=True)
def firm_delete_view(request, pk):
    firm = get_object_or_404(Firm, pk=pk)
    if request.method == 'POST':
        form = FirmSoftDeleteForm(request.POST)
        if form.is_valid():
            firm.delete = form.cleaned_data['delete_date'] 
            firm.save()
            return redirect('core:firm-list')
    else:
        form = FirmSoftDeleteForm()
    return render(request, 'firm_confirm_delete.html', {'firm': firm, 'form': form})

@login_required
def firm_delete_hard_view(request, pk):
    # Sadece süper kullanıcılar bu işlemi yapabilir
    if not request.user.is_superuser:
        return redirect('core:firm-list') # Yetkisi yoksa anasayfaya yönlendir

    firm = get_object_or_404(Firm, pk=pk)
    if request.method == 'POST':
        firm.delete_hard() # Modelimize eklediğimiz kalıcı silme metodunu çağır
        return redirect('core:firm-list')

    # Onay sayfasını gösterirken context'e bir "hard_delete" bayrağı ekleyelim
    return render(request, 'firm_confirm_delete.html', {'firm': firm, 'delete_hard': True})


def load_districts(request):
    city_id = request.GET.get('city_id')
    districts = District.objects.filter(city_id=city_id).order_by('name')
    return JsonResponse(list(districts.values('id', 'name')), safe=False)


@permission_required('core.view_personnel', raise_exception=True)
def personnel_list_view(request, firm_pk):
    firm = get_object_or_404(Firm, pk=firm_pk)
    query = request.GET.get('q')
    show_deleted = request.GET.get('show_deleted')

    if show_deleted:
        base_queryset = Personnel.objects.filter(firm=firm, delete__isnull=False)
        list_title = f"{firm.name} - Silinmiş Personeller"
    else:
        base_queryset = Personnel.objects.filter(firm=firm, delete__isnull=True)
        list_title = f"{firm.name} - Aktif Personeller"

    if query:
        base_queryset = base_queryset.filter(
            Q(name__icontains=query) |
            Q(surname__icontains=query) |
            Q(tckno__icontains=query)
        )
        list_title += f" (Arama: '{query}')"

    context = {
        'firm': firm,
        'personnel_list': base_queryset,
        'list_title': list_title,
        'is_showing_deleted': bool(show_deleted)
    }
    return render(request, 'personnel_list.html', context)


@permission_required('core.add_personnel', raise_exception=True)
def personnel_create_view(request, firm_pk):
    firm = get_object_or_404(Firm, pk=firm_pk)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            # Formu kaydetmeden önce `firm` alanını manuel olarak ata
            personnel = form.save(commit=False)
            personnel.firm = firm
            personnel.save()
            return redirect('core:personnel-list', firm_pk=firm.pk)
    else:
        # Formu, `firm` alanı bu firmaya ayarlı olarak başlat
        form = PersonnelForm(initial={'firm': firm})
    
    return render(request, 'personnel_form.html', {'form': form, 'firm': firm})


@permission_required('core.change_personnel', raise_exception=True)
def personnel_update_view(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    firm = personnel.firm
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES, instance=personnel)
        if form.is_valid():
            # Geri alma mantığını ekliyoruz
            instance = form.save(commit=False)
            if 'delete' in form.cleaned_data:
                instance.delete = form.cleaned_data['delete']
            instance.save()

            return redirect('core:personnel-list', firm_pk=firm.pk)
    else:
        form = PersonnelForm(instance=personnel)
        if personnel.related_personnel:
            form.fields['previous_tckno'].initial = personnel.related_personnel.tckno

    return render(request, 'personnel_form.html', {'form': form, 'firm': firm})


@permission_required('core.delete_personnel', raise_exception=True)
def personnel_delete_view(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    firm_pk = personnel.firm.pk # Yönlendirme için firma pk'sını al
    if request.method == 'POST':
        # Personel için de soft delete yapıyoruz (eğer modelde delete alanı varsa)
        # Eğer personel modelinde 'delete' alanı yoksa, bu satır hard delete yapar
        personnel.delete_soft() 
        return redirect('core:personnel-list', firm_pk=firm_pk)
    
    return render(request, 'personnel_confirm_delete.html', {'personnel': personnel})

@login_required
def personnel_delete_hard_view(request, pk):
    # Sadece süper kullanıcılar bu işlemi yapabilir
    if not request.user.is_superuser:
        personnel = get_object_or_404(Personnel, pk=pk)
        return redirect('core:personnel-list', firm_pk=personnel.firm.pk)

    personnel = get_object_or_404(Personnel, pk=pk)
    firm_pk = personnel.firm.pk # Yönlendirme için firma pk'sını al
    if request.method == 'POST':
        personnel.delete_hard() # Modelimize eklediğimiz kalıcı silme metodunu çağır
        return redirect('core:personnel-list', firm_pk=firm_pk)

    return render(request, 'personnel_confirm_delete.html', {'personnel': personnel, 'delete_hard': True})


@permission_required('core.view_department', raise_exception=True)
def department_list_view(request, firm_pk):
    firm = get_object_or_404(Firm, pk=firm_pk)
    departments = Department.objects.filter(firm=firm)
    context = {
        'firm': firm,
        'departments': departments
    }
    return render(request, 'department_list.html', context)


@permission_required('core.add_department', raise_exception=True)
def department_create_view(request, firm_pk):
    firm = get_object_or_404(Firm, pk=firm_pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.firm = firm
            department.save()
            return redirect('core:department-list', firm_pk=firm.pk)
    else:
        form = DepartmentForm(initial={'firm': firm})

    return render(request, 'department_form.html', {'form': form, 'firm': firm})


@permission_required('core.change_department', raise_exception=True)
def department_update_view(request, pk):
    department = get_object_or_404(Department, pk=pk)
    firm = department.firm
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('core:department-list', firm_pk=firm.pk)
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'department_form.html', {'form': form, 'firm': firm})


@permission_required('core.delete_department', raise_exception=True)
def department_delete_view(request, pk):
    department = get_object_or_404(Department, pk=pk)
    firm_pk = department.firm.pk
    if request.method == 'POST':
        department.delete()
        return redirect('core:department-list', firm_pk=firm_pk)

    return render(request, 'department_confirm_delete.html', {'department': department})

@permission_required('core.view_user', raise_exception=True)
def user_list_view(request):
    # Arama ve filtreleme için temel hazırlık
    query = request.GET.get('q')
    users = User.objects.all()

    if query:
        users = users.filter(
            Q(name__icontains=query) |
            Q(tckno__icontains=query) |
            Q(email__icontains=query)
        )

    context = {
        'users': users,
        'list_title': "Kullanıcı Listesi"
    }
    return render(request, 'user_list.html', context)


@permission_required('core.add_user', raise_exception=True)
def user_create_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Önce Django'nun standart kullanıcısını oluştur
            auth_user = AuthUser.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Sonra bizim profilimizi oluştur ve standart kullanıcıya bağla
            profile = form.save(commit=False)
            profile.auth_user = auth_user
            profile.save()
            return redirect('core:user-list')
    else:
        form = UserProfileForm()
    return render(request, 'user_form.html', {'form': form})


@permission_required('core.change_user', raise_exception=True)
def user_update_view(request, pk):
    profile = get_object_or_404(User, pk=pk)

    try:
        auth_user = profile.auth_user
    except User.auth_user.RelatedObjectDoesNotExist:
        # Eğer bu profilin bağlı olduğu bir auth_user yoksa,
        # geçici olarak boş bir tane oluşturalım ki form hata vermesin.
        # Bu durumun normalde olmaması gerekir.
        auth_user = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid() and auth_user is not None: # Sadece auth_user varsa güncelle
            profile = form.save()

            auth_user.username = form.cleaned_data['username']
            auth_user.email = form.cleaned_data['email']
            if form.cleaned_data['password']:
                auth_user.set_password(form.cleaned_data['password'])
            auth_user.save()

            return redirect('core:user-list')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'user_form.html', {'form': form})


@permission_required('core.delete_user', raise_exception=True)
def user_delete_view(request, pk):
    profile = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        try:
            # Önce bağlı auth_user'ı silmeyi dene
            profile.auth_user.delete()
        except User.auth_user.RelatedObjectDoesNotExist:
            # Eğer bağlı bir auth_user yoksa, sadece profili sil
            profile.delete()
        return redirect('core:user-list')

    return render(request, 'user_confirm_delete.html', {'user_obj': profile})