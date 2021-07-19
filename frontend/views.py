from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user_interaction.forms import PostForm
from user_interaction.models import Post

# Create your views here.

@login_required
def index(request):
    header = "Picture Perfect"
    posts = Post.objects.all().order_by("-post_date")

    return render(request, 'index.html', {'posts': posts, 'header': header})


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