# Generated by Django 5.0.4 on 2024-05-05 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatsession',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
        migrations.DeleteModel(
            name='ChatSession',
        ),
    ]
