# from django import forms
from django.forms import ModelForm
from user_interaction.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author']