from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from authentication.models import Author


# Create your views here.
def profile(request):
    ...


class ProfileView(View):

    def get(self, request):
        template = 'profile.html'
        profile_user = Author.objects.all().order_by("-date_joined")
        return render(request, template, {'profile': profile_user})