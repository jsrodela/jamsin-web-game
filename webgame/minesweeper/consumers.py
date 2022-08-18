import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

from .models import Minesweeper


class MinesweeperConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.game = None

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
                self.width = int(text_data_json['width'])
                self.height = int(text_data_json['height'])
                self.mine_cnt = int(text_data_json['num'])

            elif command == 'uncover':
                x, y = text_data_json['pos']

                if not self.game.board:
                    Minesweeper.create_board(self.game, self.width, self.height, self.mine_cnt, x, y)

                data = {'command': 'uncover', 'cells': Minesweeper.uncover(
                    self.game, x, y, [], [])[0]}
                self.send(json.dumps(data))

            elif command == 'flag':
                # TODO Mark cell as flagged
                x, y = text_data_json['pos']
                pass

            elif command == 'unflag':
                # TODO Unmark flagged cell
                x, y = text_data_json['pos']
                pass
