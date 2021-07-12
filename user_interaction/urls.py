from django.urls import path
from .views import NewPostView, PostDetailView


urlpatterns = [
    path('newpost/', NewPostView.as_view(), name='newpost'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
]