# carbon/urls.py
from django.urls import path
from . import views

app_name = 'carbon'
urlpatterns = [

    path('input/dynamic/', views.dynamic_input_view, name='dynamic-input'),
    path('api/options/<str:option_type>/', views.api_get_options, name='api-options'),
    path('api/dynamic-input/', views.api_dynamic_input, name='api-dynamic-input'),
    path('api/recent-inputs/', views.api_recent_inputs, name='api-recent-inputs'),

    # Karbon Katsayı URL'leri
    path('coefficient/', views.coefficient_list_view, name='coefficient-list'),
    path('coefficient/create/', views.coefficient_create_view, name='coefficient-create'),
    path('coefficient/<int:pk>/update/', views.coefficient_update_view, name='coefficient-update'),
    path('coefficient/<int:pk>/delete/', views.coefficient_delete_view, name='coefficient-delete'),
    
    # AJAX URL'leri
    path('ajax/get-subscopes/', views.ajax_get_subscopes, name='ajax-get-subscopes'),
    path('ajax/get-coefficient-types/', views.ajax_get_coefficient_types, name='ajax-get-coefficient-types'),

    path('management/', views.management_list_view, name='management-list'),
    path('emissionfactor/create/', views.emissionfactor_create_view, name='emissionfactor-create'),
    path('emissionfactor/<int:pk>/update/', views.emissionfactor_update_view, name='emissionfactor-update'),
    path('emissionfactor/<int:pk>/delete/', views.emissionfactor_delete_view, name='emissionfactor-delete'),
    
    # Bu satırın YORUMDA OLMADIĞINDAN emin olun:
    path('input/', views.input_list_view, name='input-list'),
    
    path('inputdata/create/', views.inputdata_create_view, name='inputdata-create'),
    path('inputdata/<int:pk>/update/', views.inputdata_update_view, name='inputdata-update'),
    path('inputdata/<int:pk>/delete/', views.inputdata_delete_view, name='inputdata-delete'),
    path('report/', views.report_list_view, name='report-list'),
    path('report/generate/', views.report_generate_view, name='report-generate'),
    path('report/<int:pk>/detail/', views.report_detail_view, name='report-detail'),
    path('excel-report/', views.excel_report_view, name='excel-report'),
]