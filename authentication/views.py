from authentication.models import Author
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from authentication.forms import SignUpForm, LoginForm
from django.views.generic import TemplateView


# Create your views here.

def signup_view(request):
    header = "Sign Up"
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_user = Author.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                avatar_image=data.get("avatar_image"),
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))  
        else:
            return HttpResponse(form.errors.values())
    form = SignUpForm()
    return render(request, 'signup_form.html', {"form": form, 'header': header})


class LoginView(TemplateView):
    header = "Login"
    
    def get(self, request):
        form = LoginForm()
        return render(request, "login_form.html", {"form": form, 'header': self.header})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
            
            return render(request, "login_form.html", {"form": form, 'header': self.header})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


def error_404_view(request, exception):
    return render(request, '404error.html')


def error_500_view(request):
    return render(request, '500error.html')


def check(request):
    ...


class FollowView(TemplateView):
    def get(self, request, follow_id):
        signed_in_user = request.user
        follow = Author.objects.filter(id=follow_id).first()
        signed_in_user.following.add(follow)
        signed_in_user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class UnfollowView(TemplateView):
    def get(self, request, unfollow_id):
        signed_in_user = request.user
        unfollow = Author.objects.filter(id=unfollow_id).first()
        signed_in_user.following.remove(unfollow)
        signed_in_user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
