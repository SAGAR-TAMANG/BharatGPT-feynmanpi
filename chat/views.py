from django.shortcuts import render
import random
from django.core.cache import cache

from dotenv import load_dotenv 
import google.generativeai as genai
import os

load_dotenv()
google_gemini_key = os.getenv("GOOGLE_GEMINI")


cards = [
  "Write a Python script#to automate sending daily email reports",
  "Suggest fun activites#to help make friends in a new city",
  "Quiz me on world capitals#to enhance my geography skills",
  "Write an email#to request a quote from local plumbers",
  "Help me pick#an outfit that will look good on camera",
  "Write a text#inviting my neighbours to a barbecue",
  "Plan a mental health day#to help me relax",
  "What is Nepal#famous for?",
  "Learn how to cook#popular Indian dishes like butter chicken",
  "Recommend me places#to visit in Mumbai for authentic street food experiences",
  "Test my knowledge on Bollywood movies#with a fun quiz",
  "Help me draft#an invitation for a traditional Indian wedding ceremony",
  "Suggest activities#for celebrating Diwali with family and friends",
  "Plan a weekend getaway#to explore historical sites in Rajasthan",
  "Teach me basic phrases#in Hindi for traveling in India",
  "What are the top#tourist attractions in Goa?",
  "Create a shopping list#for hosting a Holi party",
  "Write a review#for a local restaurant serving South Indian cuisine",
  "Design an itinerary#for a spiritual retreat in the Himalayas",
  "Share tips#for managing stress with Ayurvedic practices",
  "What is the significance#of the Taj Mahal in Indian history?",
  "Help me choose#a traditional Indian attire for a festive occasion",
  "Recommend books#by Indian authors for my reading list",
  "Create a playlist#of popular Bollywood songs for a road trip",
  "Write a speech#for Independence Day celebrations",
  "Suggest ways#to incorporate yoga into my daily routine",
  "Plan a cultural exchange#event with international students",
  "Share tips#for navigating Indian train travel",
  "What are the best#street food vendors in Delhi?",
  "Learn how to make#traditional Indian sweets like gulab jamun",
  "Recommend me movies#to watch during monsoon season",
  "Test my knowledge on Indian mythology#with a mythology quiz",
  "Help me compose#a letter of appreciation for my parents in Hindi",
  "Suggest ways#to celebrate Raksha Bandhan with my siblings",
  "Plan a pilgrimage#to visit sacred sites in Varanasi",
  "Teach me regional greetings#in languages spoken across India",
  "What are the must-try#street food delicacies in Kolkata?",
  "Create a shopping list#for a traditional Indian wedding gift",
  "Write a blog post#about my experience attending a cricket match in India",
  "Design an itinerary#for exploring the backwaters of Kerala",
  "Share remedies#for common ailments using Ayurvedic principles",
  "What is the history#behind the festival of Navratri?",
  "Help me select#a traditional Indian jewelry set for a special occasion",
  "Recommend podcasts#discussing Indian history and culture",
  "Create a playlist#of devotional songs for morning meditation",
  "Write a poem#celebrating the diversity of India's cultures",
  "Suggest activities#for a family picnic in a local park",
  "Plan a community event#to promote environmental awareness",
  "Share tips#for capturing stunning photographs of Indian landscapes",
  "What are the best#vegetarian restaurants in Chennai?",
  "Learn about the rich#culture and traditions of Assam",
  "Recommend me movies#featuring Assamese culture and landscapes",
  "Test my knowledge on#the wildlife of Kaziranga National Park",
  "Help me plan#a visit to Kaziranga National Park for wildlife safari",
  "Suggest traditional Assamese#dishes to try during my visit to Assam",
  "Explore the history#of the tea industry in Assam",
  "Teach me basic phrases#in Assamese for traveling in Assam",
  "What are the top#tourist attractions in Guwahati, Assam?",
  "Create a travel itinerary#for exploring Majuli Island, Assam",
  "Write a review#for a homestay experience in a tea estate in Assam",
  "Design an eco-tourism#program to promote sustainability in Assam",
  "Share insights#into the biodiversity of Kaziranga National Park",
  "What is the significance#of Kaziranga University in Assam's education landscape?",
  "Help me select#a souvenir from Assam to bring back home",
  "Recommend books#about the history and culture of Assam",
  "Create a playlist#featuring Assamese folk music and traditional songs",
  "Write a blog post#about my adventure exploring Kaziranga National Park",
  "Suggest activities#for a cultural immersion experience in Assam",
  "Plan a community cleanup#event along the banks of the Brahmaputra River",
  "Share tips#for responsible wildlife viewing in Kaziranga National Park",
]

def index(request):
  if request.htmx:
    print("\n\nINDEX FUNCTION RUNNING\n\n")
    print("HTMX")
    print("POST:\n", request.POST)
    message = request.POST['message']

    # To Delete Chat Session 
    # session_key = request.session.session_key
    # chat_session_key = f'chat_session_{session_key}'
    # try:
    #   print("\n\n SESSIONS CLEARED \n\n")
    #   cache.delete(chat_session_key)
    # except Exception as e:
    #   print("\n\n SESSIONS NOT CLEARED \n\n")
    #   print(e)

    session_key = request.session.session_key
    if session_key is None:
        request.session.cycle_key()
        session_key = request.session.session_key

    chat_session_key = f'chat_session_{session_key}'
    chat_session = cache.get(chat_session_key)
    if chat_session is None:
        chat_session = []
        cache.set(chat_session_key, chat_session)

    # Add user message to the chat session
    sender = request.user.username if request.user.is_authenticated else "Anonymous"
    chat_session.append((sender, message))
    cache.set(chat_session_key, chat_session)

    # Get the AI response
    ai_response = bharatGPT(message)

    # Add AI response to the chat session
    chat_session.append(("BharatGPT", ai_response))
    cache.set(chat_session_key, chat_session)

    # Extract usernames and messages separately for the frontend
    chat_messages = [{'sender': sender, 'message': message} for sender, message in chat_session]

    context = {
        'chat': chat_messages
    }

    print("Context: \n", context)
    # return render(request, 'partials/message_block.html', context=context)
    # If it's the first request, render messages.html
    return render(request, 'partials/message_block.html', context=context)
  
  cards_bold, cards_normal = card_choser()

  context = {
     'cards_bold': cards_bold,
     'cards_normal': cards_normal,
     'zipped': zip(cards_bold, cards_normal)
  }

  print(context)
  
  return render(request, 'index.html', context=context)

def chat_blob(request):
  print("\n\nCHAT BLOB FUNCTION RUNNING\n\n")
  if request.htmx:
    print("HTMX")
    print("POST:\n", request.POST)
    message = request.POST['message']
    
    session_key = request.session.session_key
    if session_key is None:
        request.session.cycle_key()
        session_key = request.session.session_key

    chat_session_key = f'chat_session_{session_key}'
    chat_session = cache.get(chat_session_key)
    if chat_session is None:
        chat_session = []
        cache.set(chat_session_key, chat_session)

    # Add user message to the chat session
    sender = request.user.username if request.user.is_authenticated else "Anonymous"
    chat_session.append((sender, message))
    cache.set(chat_session_key, chat_session)

    chat_messages = [message for sender, message in chat_session]

    print("\n\nThis is the output:\n\n", chat_session)

    # Create History
    history = history_creator(chat_session)

    # Get the AI response
    ai_response = bharatGPT(message, history=[])

    # Add AI response to the chat session
    chat_session.append(("BharatGPT", ai_response))
    cache.set(chat_session_key, chat_session)

    # Extract usernames and messages separately for the frontend
    chat_messages = [{'sender': sender, 'message': message} for sender, message in chat_session]

    context = {
        'chat': chat_messages
    }

    print("Context: \n", context)
    # return render(request, 'partials/message_block.html', context=context)
    # If it's the first request, render messages.html
    return render(request, 'partials/chat_blob.html', context=context)

def card_choser():
  chosen = random.sample(cards, 4)

  bold_texts = []
  normal_texts = []

  for card in chosen:
      parts = card.split("#")
      bold_texts.append(parts[0])
      normal_texts.append(parts[1])

  return bold_texts, normal_texts

# Generative Non-Chat Model

# def bharatGPT(message, history=[]):
#     genai.configure(api_key=google_gemini_key)
#     model = genai.GenerativeModel('gemini-pro')
#     messages = []
#     messages.append({'role':'user', 'parts': ["From now onwards, I have given you a name called 'BharatGPT'. You are to use this name wherever you go."]})
#     messages = [
#         {'role':'user', 'parts': [message]}
#     ]
#     response = model.generate_content(messages)

#     messages.append({'role':'model', 'parts':[response.text]})

#     return response.text

# Chat Model

def bharatGPT(message, history=[]):
    genai.configure(api_key=google_gemini_key)
    model = genai.GenerativeModel('gemini-pro')

    history = []

    
    chat = model.start_chat(history=history)

    prompt = f'''
    BharatGPT is India's first Large Language Model (LLM) which in the backend is powered by the Google's Gemini. If anybody asks you what you are, then you will mention that you are the first LLM Developed in India by the Feynman Pi (Founded By Sagar Tamang). Now begins the converstaion:\n\n
    User: {message}
    BharatGPT:
    ''' 

    response = chat.send_message(prompt)

    print(response.text)
    print(chat.history)
    return response.text

def history_creator(history):
  print("\nHISTORY\n", history)
  
import json
from django.http import JsonResponse
from django.conf import settings

def assetlinks_json(request):
    file_path = os.path.join(settings.STATIC_ROOT, '.well-known', 'assetlinks.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)



def test(request):
   return render(request, 'tests.html')