from django import forms
from authentication.models import Author
from django.forms import ModelForm
from user_interaction.models import Post


class PostForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()


# class ImageForm(forms.Form):
#     image = forms.FileField()
