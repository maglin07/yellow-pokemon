from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class Author(AbstractUser):
    avatar_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username
