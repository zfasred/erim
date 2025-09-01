# carbon/urls.py
from django.urls import path
from . import views

app_name = 'carbon'
urlpatterns = [
    path('management/', views.management_list_view, name='management-list'),
    path('emissionfactor/create/', views.emissionfactor_create_view, name='emissionfactor-create'),
    path('emissionfactor/<int:pk>/update/', views.emissionfactor_update_view, name='emissionfactor-update'),
    path('emissionfactor/<int:pk>/delete/', views.emissionfactor_delete_view, name='emissionfactor-delete'),
    path('input/', views.input_list_view, name='input-list'),
    path('inputdata/create/', views.inputdata_create_view, name='inputdata-create'),
    path('inputdata/<int:pk>/update/', views.inputdata_update_view, name='inputdata-update'),
    path('inputdata/<int:pk>/delete/', views.inputdata_delete_view, name='inputdata-delete'),
    path('report/', views.report_list_view, name='report-list'),
    path('report/generate/', views.report_generate_view, name='report-generate'),
    path('report/<int:pk>/detail/', views.report_detail_view, name='report-detail'),
]