import uuid
import datetime
from django.contrib.auth.models import User
from django.db import models

from .omok import OmokGame

class Omok(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='omok_creator')
    opponent = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='omok_opponent', null=True)

    # Game log
    moves = models.JSONField(null=True)
    # Chat log
    chat = models.JSONField(null=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    created = models.DateTimeField(default=datetime.datetime.now)
    completed = models.DateTimeField(null=True)

    def create(user):
        game = Omok(creator=user)
        game.save()
        return game

    def complete(self):
        self.completed = datetime.datetime.now()
        self.save()

    def create_board(self):
        self.game = OmokGame()
