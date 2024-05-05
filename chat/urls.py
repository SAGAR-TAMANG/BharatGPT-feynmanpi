from django.urls import path
from .views import index, chat_blob, test

urlpatterns = [
  path('', index, name='index'),
  path('chat', chat_blob, name='chatBharatGPT'),
  path('test', test, name='test'),
]