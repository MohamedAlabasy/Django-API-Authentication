# from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Doctors(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    username = None  # To override username and make it = none

    # To make Django login with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
