from django.db import models
from django.utils import timezone
from authentication.models import Author

# Create your models here.


class Post(models.Model):
    post_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __str__(self):
        return self.title
