from django.contrib import admin
from django.urls import path, include, path
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('', include('pwa.urls')), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
