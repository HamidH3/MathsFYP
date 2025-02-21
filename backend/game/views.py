from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile, Leaderboard
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def index_view(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def pygame_view(request):
    return 
# render(request, "game/pygame_game.html")

def list_users(request):
    # users = UserProfile.objects.all()
    # return render(request, 'game/users_list.html', {'users': users})
    users = UserProfile.objects.all()  # Fetch all users from the database
    user_data = [user.as_dict() for user in users]  # Assuming you have as_dict() method to serialize
    return JsonResponse(user_data, safe=False) 


@csrf_exempt
def username_api_view(request):
    if request.method == 'GET':
        return JsonResponse({
        'usernames': [username.as_dict() 
        for username in UserProfile.objects.all()]
        })
    if request.method == 'POST':
        POST = json.loads(request.body)
        print(f"Received username: {POST['username']}")
        username = UserProfile.objects.create(
            username = POST['username']
        )
        return JsonResponse(username.as_dict(), status=201)
    return HttpResponse(status=405)
