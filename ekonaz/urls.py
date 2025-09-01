# ekonaz/urls.py - OLMASI GEREKEN DOĞRU HALİ

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', include('core.urls')),
    path('carbon/', include('carbon.urls')),
]

# Medya dosyalarını sunmak için gereken blok BURADA, dosyanın en sonunda olmalı
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)