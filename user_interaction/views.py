from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import PostForm
from .models import Post


# Create your views here.
class PostDetailView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        post = Post.objects.filter(id=id).first()
        return render(request, 'profile.html', {'post': post})


class NewPostView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        template = 'generic_form.html'
        form = PostForm()
        return render(request, template, {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.create(
                    post_date=data.get('post_date'),
                    title=data.get('title'),
                    description=data.get('description'),
                    author=data.get('author'),
                    # author=request.user,
                    likes=data.get('likes'),
                    dislikes=data.get('dislikes'),
                )
                return render(request, 'profile.html', {'form': form})
