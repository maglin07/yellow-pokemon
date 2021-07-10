from django import forms
from authentication.models import Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar_image']
