from django import forms
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class Author(AbstractUser):
    avatar_image = models.ImageField(null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username
