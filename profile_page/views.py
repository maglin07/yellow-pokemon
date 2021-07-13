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
        posts = Post.objects.filter(author=profile_user).order_by("-post_date")
        return render(request, template, {'profile': profile_user, 'posts': posts})


@login_required
def ProfileUpdateView(request, user_id):
    author = Author.objects.get(id=user_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            author.username = data['username']
            author.email = data['email']
            author.first_name = data['first_name']
            author.last_name = data['last_name']
            author.save()
        return HttpResponseRedirect(reverse("profile", args=(user_id,)))

    form = AuthorForm(initial={
        'username': author.username,
        'email': author.email,
        'first_name': author.first_name,
        'last_name': author.last_name
    })
    return render(request, 'generic_form.html', {'form': form})
