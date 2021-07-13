from django.urls import path
from .views import NewPostView, PostDetailView, PostDeleteView, CommentDeleteView
from frontend.views import likes_view, dislikes_view


urlpatterns = [
    path('newpost/', NewPostView.as_view(), name='newpost'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:post_id>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:id>/likes/', likes_view, name='like_view'),
    path('post/<int:id>/dislikes/', dislikes_view, name='dislike_view'),
    path('comment/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    
]