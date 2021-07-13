from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user_interaction.forms import PostForm
from user_interaction.models import Post

# Create your views here.

@login_required
def index(request):

    return render(request, 'index.html')

@login_required
def image_upload_view(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post_data = post_form.cleaned_data
            new_post = Post.objects.create(
                author=post_data['author'],
                title=post_data['title'],
                description=post_data['description'],
                image=post_data['image']
            )
            return render(request, 'upload.html', {'post_form': post_form})
        return HttpResponseRedirect(request.GET.get
                                    ('next', reverse('homepage')))        
    else:
        post_form = PostForm()
    return render(request, 'upload.html', {'post_form': post_form})


def likes_view(request, id):
    post = Post.objects.get(id=id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', ""))


def dislikes_view(request, id):
    post = Post.objects.get(id=id)
    post.dislikes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', ""))