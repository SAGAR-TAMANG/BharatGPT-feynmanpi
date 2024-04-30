from django.contrib import admin
from django.urls import path
from .api import client

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', client.urls),
]
