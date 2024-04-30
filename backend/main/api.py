from ninja import NinjaAPI, Schema
from django.http import JsonResponse

client = NinjaAPI()

class ChatSchema(Schema):
  id: str
  message: str

@client.get("/hello")
def hello(request):
  return JsonResponse({
    'message': 'Hello World'
  })

@client.post("/chat", response=ChatSchema)
def chat_gemini(request):
  return JsonResponse({
    'message': 'API Requst to the GPT sent.'
  })