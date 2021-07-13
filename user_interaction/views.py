from django.shortcuts import render, reverse, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.http import HttpResponseForbidden


# Create your views here.
class PostDetailView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, post_id):
        posts = Post.objects.filter(id=post_id)
        comments = Comment.objects.filter(post_id=post_id)
        form = CommentForm()
        return render(request, 'post_detail.html', {'posts': posts, 'comments': comments, 'form': form})
    
    def post(self, request, post_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            current_post = Post.objects.get(id=post_id)
            data = form.cleaned_data
            comment = Comment.objects.create(
                author=request.user,
                post=current_post,
                text=data['text'],
            )
        return HttpResponseRedirect(reverse('post_detail', args=(post_id,)))


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
                    author=request.user,
                    image=data['image']
                )
                return HttpResponseRedirect(reverse('homepage'))


class PostDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.delete()
        return HttpResponseRedirect(reverse('homepage'))


class CommentDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', ""))


def CommentEditView(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    post_id = comment.post.id

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment.text = data['text']
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=(post_id,)))
            
    form = CommentForm(initial={
        'text' : comment.text
    })
    return render(request, 'post_detail.html', {'form': form})
