from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Contact(models.Model):
    user = models.ForeignKey(User,models.SET_NULL,null=True,blank=True)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,blank=True)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1048)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username