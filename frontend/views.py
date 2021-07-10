from django.shortcuts import render, reverse, HttpResponseRedirect
from user_interaction.forms import ImageForm, PostForm
from user_interaction.models import Post
from media.models import Image

# Create your views here.


def index(request):

    return render(request, 'index.html')

def image_upload_view(request):
    if request.method == 'POST':
        image_form = []
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if post_form.is_valid() and image_form.is_valid():
            # form.save()
            post_data = post_form.cleaned_data
            new_post = Post.objects.create(author = post_data['author'], title =post_data['title'], description = post_data['description'])
            image_data=image_form.cleaned_data
            new_image = Image.objects.create(post= new_post, author=post_data['author'], image = image_data['image'])
            # image = image_form.instance
            return render(request, 'upload.html', {'post_form': post_form, 'image_form': image_form})
        return HttpResponseRedirect(request.GET.get
                                    ('next', reverse('homepage')))        
    else:
        post_form = PostForm()
        image_form = ImageForm()
    return render(request, 'upload.html', {'post_form': post_form, 'image_form': image_form})


# def image_upload_view(request):
#     if request.method == 'POST':
#         form = []
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             image = form.instance
#             return render(request, 'upload.html', {'form': form, 'image':
#                                                                 image})
#         return HttpResponseRedirect(request.GET.get
#                                     ('next', reverse('homepage')))        
#     else:
#         form = ImageForm()
#     return render(request, 'upload.html', {'form': form})