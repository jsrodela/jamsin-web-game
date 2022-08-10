import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

from .models import Minesweeper


class MinesweeperConsumer(WebsocketConsumer):
    def connect(self):
        user = User.objects.get(username=self.scope['user'])
        game = Minesweeper.create(user)
        self.game = game

        self.accept()

    def disconnect(self, close_code):
        self.game.complete()

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        if 'command' in text_data_json.keys():
            command = text_data_json['command']
            if command == 'set':
                # TODO Create new board
                size = text_data_json['size']
                mine_cnt = text_data_json['num']
                pass
            if command == 'uncover':
                # TODO Uncover selected cell and send result
                x, y = text_data_json['pos']
                pass
            if command == 'flag':
                # TODO Mark cell as flagged
                x, y = text_data_json['pos']
                pass
            if command == 'unflag':
                # TODO Unmark flagged cell
                x, y = text_data_json['pos']
                pass
