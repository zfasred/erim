from django.urls import path
from . import views

app_name = 'carbon'

urlpatterns = [

    path('api/coefficient-names/', views.api_get_coefficient_names, name='api-coefficient-names'),

    # Karbon Yönetim
    path('management/', views.management_list_view, name='management-list'),
    
    # Karbon Katsayı Yönetimi - YENİ EKLENECEK
    path('coefficient/', views.coefficient_list_view, name='coefficient-list'),
    path('coefficient/create/', views.coefficient_create_view, name='coefficient-create'),
    path('coefficient/<int:pk>/update/', views.coefficient_update_view, name='coefficient-update'),
    path('coefficient/<int:pk>/delete/', views.coefficient_delete_view, name='coefficient-delete'),
    
    # Emisyon Faktörleri
    path('emissionfactor/create/', views.emissionfactor_create_view, name='emissionfactor-create'),
    path('emissionfactor/<int:pk>/update/', views.emissionfactor_update_view, name='emissionfactor-update'),
    path('emissionfactor/<int:pk>/delete/', views.emissionfactor_delete_view, name='emissionfactor-delete'),
    
    # Karbon Girdi - YENİ SİSTEM
    path('input/', views.input_list_view, name='input-list'),
    path('input/dynamic/', views.dynamic_input_view, name='dynamic-input'),
    
    # API endpoints
    path('api/options/<str:option_type>/', views.api_get_options, name='api-options'),
    path('api/dynamic-input/', views.api_dynamic_input, name='api-dynamic-input'),
    path('api/dynamic-input/<int:input_id>/', views.api_dynamic_input, name='api-dynamic-input-delete'),
    path('api/recent-inputs/', views.api_recent_inputs, name='api-recent-inputs'),
    
    # Rapor
    path('report/', views.report_list_view, name='report-list'),
]