"""picture_perfect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from frontend import views
from profile_page.urls import urlpatterns as profile_page_urls
from user_interaction.urls import urlpatterns as user_interaction_urls
from authentication.views import check, signup_view, LoginView, logout_view, FollowView, UnfollowView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('check/', check, name='check'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('following/<int:follow_id>/', FollowView.as_view()),
    path('unfollowing/<int:unfollow_id>/', UnfollowView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += profile_page_urls
urlpatterns += user_interaction_urls


handler404 = "authentication.views.error_404_view"
handler500 = "authentication.views.error_500_view"