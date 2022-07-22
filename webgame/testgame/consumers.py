import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TestgameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'testgame'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if 'message' in text_data_json.keys():
            message = text_data_json['message']

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

        if 'play' in text_data_json.keys():
            move = text_data_json['play']
            client = self.scope['client']

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'game_message',
                    'client': client,
                    'move': move
                }
            )

    # Receive message from room group

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def game_message(self, event):
        if event['client'] == self.scope['client']:
            return

        move = event['move']
        await self.send(text_data=json.dumps({
            'move': move
        }))
