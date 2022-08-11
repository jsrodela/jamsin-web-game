import uuid
import datetime
from django.contrib.auth.models import User
from django.db import models
import random
import json


class Minesweeper(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='minesweeper_creator')

    # JSON list
    # mine: -1 / number: number of mines near 3x3
    board = models.JSONField(default=dict)

    # Save content as json string
    moves = models.TextField(null=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    created = models.DateTimeField(default=datetime.datetime.now)
    completed = models.DateTimeField(null=True)

    def create(user):
        game = Minesweeper(creator=user)
        game.save()
        return game

    def complete(self):
        self.completed = datetime.datetime.now()
        self.save()

    def create_board(self, size, mine_cnt):
        board_arr = [[0 for _ in range(size)] for _ in range(size)]

        # Place mine
        for _ in range(mine_cnt):
            x = random.randrange(0, size - 1)
            y = random.randrange(0, size - 1)
            board_arr[x][y] = -1

        # 좌상단 -> 우하단
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]

        # Generate number
        for i in range(size):
            for j in range(size):
                if board_arr[i][j] == -1:
                    continue

                cnt = 0
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]

                    if x < 0 or x >= size or y < 0 or y >= size:
                        continue

                    if board_arr[x][y] == -1:
                        cnt += 1
                board_arr[i][j] = cnt

        self.board = json.dumps(board_arr)
        self.save()

    def uncover(self, x, y, uncov_arr, done_arr):
        board_arr = json.loads(self.board)
        done_arr.append((x, y))
        # print(done_arr)
        if board_arr[x][y] == 0:
            dx = [-1, 0, 1, -1, 1, -1, 0, 1]
            dy = [-1, -1, -1, 0, 0, 1, 1, 1]
            for k in range(8):
                tx = x + dx[k]
                ty = y + dy[k]

                if tx < 0 or tx >= len(board_arr) or ty < 0 or ty >= len(board_arr[0]):
                    continue

                done = False
                for px, py in done_arr:
                    if px == tx and py == ty:
                        done = True
                        break
                if done:
                    continue

                uncov_arr, done_arr = self.uncover(tx, ty, uncov_arr, done_arr)

        uncov_arr.append({'x': x, 'y': y, 'value': board_arr[x][y]})
        return uncov_arr, done_arr
