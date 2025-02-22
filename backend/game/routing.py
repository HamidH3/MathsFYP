'''
Here, routing further organizes WebSocket routing, specifically for
 the game app, keeping the architecture modular.
'''

from django.urls import re_path
from .consumers import GameConsumer

websocket_urlpatterns = [
    re_path(r"ws/game/$", GameConsumer.as_asgi()),
]
