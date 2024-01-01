from django.db import models
from django.contrib.auth import get_user_model
import board.models

User = get_user_model()

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

