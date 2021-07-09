from django.shortcuts import render, reverse, HttpResponseRedirect
from user_interaction.forms import ImageForm, PostForm
from user_interaction.models import Post
from media.models import Image

# Create your views here.


def index(request):

    return render(request, 'index.html')

def image_upload_view(request):
    if request.method == 'POST':
        form = []
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if post_form.is_valid() and image_form.is_valid():
            # form.save()
            data = post_form.cleaned_data
            new_post = Post.objects.create(author = data['author'], title = data['title'], description = data['description'])
            # data=image_form.cleaned_data
            # Photo = form.instance
            return render(request, 'upload.html', {'post_form': post_form})
        return HttpResponseRedirect(request.GET.get
                                    ('next', reverse('homepage')))        
    else:
        post_form = PostForm()
    return render(request, 'upload.html', {'post_form': post_form})