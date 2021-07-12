from django import forms
from authentication.models import Author
from django.forms import ModelForm
from user_interaction.models import Post, Comment


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea, max_length=250)
    image = forms.ImageField()


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']