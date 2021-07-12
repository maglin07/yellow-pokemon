from django.urls import path
from .views import NewPostView, PostDetailView, PostDeleteView, CommentDeleteView


urlpatterns = [
    path('newpost/', NewPostView.as_view(), name='newpost'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:post_id>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]