from django.urls import path
from profile_page.views import ProfileView, ProfileUpdateView

urlpatterns = [
    path('profile/<int:user_id>/update/', ProfileUpdateView, name='profile_update'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
]