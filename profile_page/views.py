from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.views.generic import View

from authentication.models import Author
from user_interaction.models import Post
from authentication.forms import AuthorForm


# Create your views here.

class ProfileView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, user_id: int):
        template = 'profile.html'
        profile_user = Author.objects.get(id=user_id)
        header = profile_user.username
        posts = Post.objects.filter(author=profile_user).order_by("-post_date")
        post_count = posts.count()
        follower_count = profile_user.author_set.all().count()
        following_count = profile_user.following.count()
        following_profile_user = False
        if profile_user in request.user.following.all():
            following_profile_user = True
        return render(request, template, {
            'profile': profile_user,
            'posts': posts,
            'post_count': post_count,
            'follower_count': follower_count,
            'following_count': following_count,
            'header': header,
            'following_profile_user': following_profile_user,
        })


@login_required
def ProfileUpdateView(request, user_id):
    header = "Edit Profile"
    author = Author.objects.get(id=user_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            author.username = data['username']
            author.email = data['email']
            author.first_name = data['first_name']
            author.last_name = data['last_name']
            author.avatar_image = data['avatar_image']
            author.save()
        return HttpResponseRedirect(reverse("profile", args=(user_id,)))

    form = AuthorForm(initial={
        'username': author.username,
        'email': author.email,
        'first_name': author.first_name,
        'last_name': author.last_name,
        'avatar_image': author.avatar_image,
    })
    return render(request, 'signup_form.html', {'form': form, 'header': header})
