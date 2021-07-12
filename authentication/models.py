from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class Author(AbstractUser):
    avatar_image = models.ImageField(upload_to='images/', null=True, blank=True)
    username = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.username
