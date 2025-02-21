from django.urls import path

# from . import views
from .views import pygame_view, username_api_view, list_users, index_view
# index_view
from .models import UserProfile, Leaderboard

#127.0.0.1:8000 port
urlpatterns = [
    path("", index_view, name="index"),
    # path('', pygame_view, name='pygame'),
    # path('pygame/',  pygame_view, name='pygame'),
    path('users/create/', username_api_view, name='user_profile'),
    path('users/', list_users, name='list_users'),
    
]