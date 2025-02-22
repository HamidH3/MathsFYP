'''
Here, the routing maps WebSocket connections to the appropriate GameConsumer.
Configures WebSocket URL patterns (ws://localhost:8000/ws/game/).
'''

from django.urls import re_path
from game.consumers import GameConsumer

websocket_urlpatterns = [
    re_path(r"ws/game/$", GameConsumer.as_asgi()),  # WebSocket route for the game
]
