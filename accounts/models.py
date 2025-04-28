from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True
    )
    phone_number = models.CharField(
        max_length=50,
        blank=True
    )
    avatar = models.ImageField(
        upload_to='users/',
        blank=True
        )
    birth_date = models.DateField(
        blank=True,
        null=True
    )