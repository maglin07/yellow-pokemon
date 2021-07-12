from django.urls import path
from .views import NewPostView, PostDetailView, PostDeleteView


urlpatterns = [
    path('newpost/', NewPostView.as_view(), name='newpost'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:post_id>/delete', PostDeleteView.as_view(), name='post_delete')
]