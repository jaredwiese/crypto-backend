from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related
import uuid


class CustomUser(AbstractUser):

    def __str__(self):
        return self.email

class SecretMessage(models.Model):
    secret_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    message_name = models.CharField(max_length=50, unique=True)
    cipher_text = models.TextField(blank = True)
    decrypt_key = models.TextField(blank = True)
    user_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'secretmessages')

    def __str__(self):
        return self.message_name
