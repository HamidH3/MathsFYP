from django.contrib import admin
from .models import UserProfile, Leaderboard

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    The UserProfileAdmin class is responsible for providing a view of the UserProfile
    model in the Django admin interface.

    Attributes (all tuples)
    ----------
    - list_display: Specifies fields to display in the admin list view.
    - search_fields: Allows the admin to search for data by username.
    """
    list_display = ('id', 'username')  # Display ID and username
    search_fields = ('username',)  # Allow search by username

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """
    The LeaderboardAdmin class provides an interface for managing leaderboard data in
    the Django admin interface.

    Attributes (all tuples)
    ----------
    - list_display: Specifies fields to display in the admin list view.
    - list_filter: Allows the admin to filter the leaderboard by score.
    - search_fields: Allows the admin to search for data by username.
    """
    list_display = ('user', 'score')  # Display user and score in the list view
    list_filter = ('score','user__username')  # Filter by score
    search_fields = ('user__username',)  # Search by username of the user
