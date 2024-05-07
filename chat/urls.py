from django.urls import path
from .views import index, chat_blob, assetlinks_json, test

urlpatterns = [
  path('', index, name='index'),
  path('chat', chat_blob, name='chatBharatGPT'),
  path('test', test, name='test'),
  path('.well-known/assetlinks.json', assetlinks_json, name='assetlinks_json'),
]