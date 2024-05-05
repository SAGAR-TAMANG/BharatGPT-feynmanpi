# from django.db import models
# from django.contrib.auth.models import User

# class ChatSession(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     session_id = models.CharField(max_length=100)

# class ChatMessage(models.Model):
#     session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

