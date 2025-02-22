'''
here, we define a WebSocket consumer (GameConsumer) that handles connections, disconnections,
and messages being sent to and from server to client.
Uses AsyncWebsocketConsumer from Django Channels to send and receive game frames.
The code also calls get_game_frame() from game.py to capture and send Pygame frames from the backend to the frontend.
'''
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from game.game import get_game_frame

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "game_channel"

        # Connect and join game group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()  # Accept WebSocket connection
        print("WebSocket connected")

    async def disconnect(self, close_code):
        # Disconnect and leave game group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("WebSocket disconnected")

    async def receive(self, text_data):
        """
        Handles incoming WebSocket messages.
        If the client sends a request (e.g., 'get_frame'), return a game frame.
        """
        try:
            data = json.loads(text_data)  # Parse JSON message
            print("Received:", data)

            if data.get("action") == "get_frame":
                frame_data = get_game_frame()  # Get the game frame (base64)
                await self.send_game_frame(frame_data)
            else:
                print("Unknown action:", data.get("action"))

        except json.JSONDecodeError:
            print("Invalid JSON received:", text_data)

    async def send_game_frame(self, frame_data):
        """Sends game frames as a JSON object to the frontend"""
        if frame_data:
            print("Sending frame data...")  # Debugging
            await self.send(text_data=json.dumps({"frame": frame_data}))
