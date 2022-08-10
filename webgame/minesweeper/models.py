import uuid
import datetime
from django.contrib.auth.models import User
from django.db import models


class Minesweeper(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='minesweeper_creator')

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
