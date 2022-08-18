import json
import random
from typing import Dict
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync

from .omok import OmokGame

from .models import Omok

ongoing_games: Dict[str, OmokGame] = {}
waiting_games: Dict[str, OmokGame] = {}


class OmokConsumer(WebsocketConsumer):
    def connect(self):
        start_game = False
        color_changed = False

        # Search for game
        games = Omok.objects.filter(white=None)
        user = User.objects.get(username=self.scope['user'])
        for game in games:
            if game.black != user:
                start_game = True
                self.color = 'white'

                # Pick color
                if random.randint(0, 1):
                    game.white = user
                else:
                    color_changed = True
                    game.white = game.black
                    game.black = user
                game.save()
                break
        else:
            # Create new game
            game = Omok.create(user)
            waiting_games[game.id] = OmokGame()
            self.color = 'black'

        self.game = game
        self.room_group_name = f'omok_{game.id}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({'room_id': str(self.game.id)}))

        if color_changed:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'color.changed',
                }
            )
        if start_game:
            ongoing_games[game.id] = waiting_games[game.id]
            del waiting_games[game.id]
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'start.game',
                }
            )

    def disconnect(self, close_code):
        if self.game.white == None:
            self.game.delete()
        else:
            self.game.complete()
            print(self.game.created, self.game.completed)

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

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        client = self.scope['client']

        if 'command' in text_data_json.keys():
            if text_data_json['command'] == 'place':
                pos = text_data_json['pos']

                if not ongoing_games[self.game.id].move(*pos):
                    return

                # TODO Check result and send if the game is finished
                ongoing_games[self.game.id].check_result()

                # Send move position to group
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'game.message',
                        'client': client,
                        'move': pos,
                        'color': self.color,
                    }
                )

    # Receive message from room group

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def color_changed(self, event):
        if self.color == 'black':
            self.color = 'white'
        else:
            self.color = 'black'

    def game_message(self, event):
        if 'move' in event.keys():
            pos = event['move']
            self.send(text_data=json.dumps({
                'move': pos,
                'color': event['color'],
            }))

    def leave(self, event):
        if event['client'] == self.scope['client']:
            return
        self.close()

    def start_game(self, event):
        if self.color == 'black':
            opponent_color = 'white'
        else:
            opponent_color = 'black'
        self.send(text_data=json.dumps({
            'init': True,
            'color': self.color,
            'opponentColor': opponent_color,
        }))
