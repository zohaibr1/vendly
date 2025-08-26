from django.urls import path
from .views.auth_view import RegisterView
from .views.login_view import LoginView
from .views.logout_view import LogoutView
from .views.profile_view import UserProfileView

urlpatterns = [
path('/register/',RegisterView.as_view(), name='register'),
path('/login/',LoginView.as_view(), name='login'),
path('/logout/',LogoutView.as_view(), name='logout'),
path('/profile/',UserProfileView.as_view(), name='profile'),
]