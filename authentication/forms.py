from django import forms
from authentication.models import Author

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'username', 'password', 'avatar_image']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)