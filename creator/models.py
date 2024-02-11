from django.db import models
from django.contrib.auth import get_user_model
from gallery.models import Gallery

User = get_user_model()

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "creator")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        gallery = Gallery(creator=self)
        gallery.save()
        return self.id


    

