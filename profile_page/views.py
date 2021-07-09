from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from authentication.models import Author
from user_interaction.models import Post


# Create your views here.
def profile(request):
    ...


class ProfileView(View):

    def get(self, request, id):
        template = 'profile.html'
        profile_user = Author.objects.get(id=id)
        posts = Post.objects.filter(author=profile_user)
        return render(request, template, {'profile': profile_user, 'posts': posts})


class ProfileEdit(View):
    ...
