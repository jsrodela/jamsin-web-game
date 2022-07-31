import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync

from .models import Game


class TestgameConsumer(WebsocketConsumer):
    def connect(self):
        # Search for game
        games = Game.objects.filter(opponent=None)
        user = User.objects.get(username=self.scope['user'])
        for game in games:
            if game.creator != user:
                game.opponent = user
                game.save()
                break
        else:
            # Create new game
            game = Game.create(user)

        self.game = game
        self.room_group_name = f'testgame_{game.id}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({'room_id': str(self.game.id)}))

    def disconnect(self, close_code):
        if self.game.opponent == None:
            self.game.delete()
        else:
            self.game.complete()
            print(self.game.created,self.game.completed)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'leave',
                'client': self.scope['client']
            }
        )

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if 'message' in text_data_json.keys():
            message = text_data_json['message']

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat.message',
                    'message': message
                }
            )

        if 'play' in text_data_json.keys():
            move = text_data_json['play']
            client = self.scope['client']

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'game.message',
                    'client': client,
                    'move': move
                }
            )

    # Receive message from room group

    def chat_message(self, event):
        print(self.scope['user'], event['message'])
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def game_message(self, event):
        if event['client'] == self.scope['client']:
            return

        move = event['move']
        self.send(text_data=json.dumps({
            'move': move
        }))

    def leave(self, event):
        if event['client'] == self.scope['client']:
            return
        self.close()
