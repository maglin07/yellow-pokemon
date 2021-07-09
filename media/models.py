from django.db import models
from django.db.models.deletion import CASCADE
from authentication.models import Author
from user_interaction.models import Post
# Create your models here.


class Image(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField(default="Describe your photo")

    def __str__(self):
        return f'{self.author} - {self.id}'
