from django import forms
from authentication.models import Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar_image']


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'username', 'password', 'avatar_image']
      

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={"placeholder": 'Password'}))
