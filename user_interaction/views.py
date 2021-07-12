from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import PostForm
from .models import Post, Comment


# Create your views here.
class PostDetailView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, post_id):
        posts = Post.objects.filter(id=post_id)
        comments = Comment.objects.filter(post_id=post_id)
        return render(request, 'post_detail.html', {'posts': posts, 'comments': comments})


class NewPostView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        template = 'generic_form.html'
        form = PostForm()
        return render(request, template, {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.create(
                    title=data.get('title'),
                    description=data.get('description'),
                    # author=data.get('author'),
                    author=request.user,
                    image=data['image']
                )
                return render(request, 'profile.html', {'form': form})
