from django.urls import path
from profile_page.views import ProfileView

urlpatterns = [
    path('profile/<int:id>/', ProfileView.as_view(), name='profile'),
]