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
                size = int(text_data_json['size'])
                mine_cnt = int(text_data_json['num'])

                Minesweeper.create_board(self.game, size, mine_cnt)
                pass

            elif command == 'uncover':
                # TODO Uncover selected cell and send result
                print(text_data_json['pos'])
                x, y = text_data_json['pos']

                data = {'command': 'uncover', 'cells': Minesweeper.uncover(self.game, x, y, [], [])[0]}
                self.send(json.dumps(data))
                print(data)
                pass

            elif command == 'flag':
                # TODO Mark cell as flagged
                x, y = text_data_json['pos']
                pass

            elif command == 'unflag':
                # TODO Unmark flagged cell
                x, y = text_data_json['pos']
                pass
