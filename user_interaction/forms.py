from django import forms
from authentication.models import Author


# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ("author", "post", "image" 'description')
#         Widgets = {
#             'description': forms.CharField(widget=forms.Textarea),
#             'image': forms.FileField()

class PostForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    title = forms.CharField(max_length=50)
    Description = forms.CharField(widget=forms.Textarea)



class ImageForm(forms.Form):
    image = forms.FileField()
