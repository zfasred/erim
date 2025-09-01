# core/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path('portal/', views.portal_view, name='portal'),

    # Firma URL'leri
    path('firms/', views.firm_list_view, name='firm-list'),
    path('firms/add/', views.firm_create_view, name='firm-add'),
    path('firms/edit/<int:pk>/', views.firm_update_view, name='firm-update'),
    path('firms/delete/<int:pk>/', views.firm_delete_view, name='firm-delete'),
    path('firms/delete-hard/<int:pk>/', views.firm_delete_hard_view, name='firm-delete-hard'),

    # AJAX URL
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),

    # Personel URL'leri (Tek sefer)
    path('firm/<int:firm_pk>/personnel/', views.personnel_list_view, name='personnel-list'),
    path('firm/<int:firm_pk>/personnel/add/', views.personnel_create_view, name='personnel-add'),
    path('personnel/edit/<int:pk>/', views.personnel_update_view, name='personnel-update'),
    path('personnel/delete/<int:pk>/', views.personnel_delete_view, name='personnel-delete'),
    path('personnel/delete-hard/<int:pk>/', views.personnel_delete_hard_view, name='personnel-delete-hard'),

    # Department URLs (added)
    path('firm/<int:firm_pk>/departments/', views.department_list_view, name='department-list'),
    path('firm/<int:firm_pk>/departments/add/', views.department_create_view, name='department-add'),
    path('departments/edit/<int:pk>/', views.department_update_view, name='department-update'),
    path('departments/delete/<int:pk>/', views.department_delete_view, name='department-delete'),

    # User managements
    path('users/', views.user_list_view, name='user-list'),
    path('users/add/', views.user_create_view, name='user-add'),
    path('users/edit/<int:pk>/', views.user_update_view, name='user-update'),
    path('users/delete/<int:pk>/', views.user_delete_view, name='user-delete'),

    # Çıkış
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]