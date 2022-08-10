import uuid
import datetime
from django.contrib.auth.models import User
from django.db import models


class Testgame(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='testgame_creator')
    opponent = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='testgame_opponent', null=True)

    # Save content as json string
    moves = models.TextField(null=True)
    chat = models.TextField(null=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    created = models.DateTimeField(default=datetime.datetime.now)
    completed = models.DateTimeField(null=True)

    def create(user):
        game = Testgame(creator=user)
        game.save()
        return game

    def complete(self):
        self.completed = datetime.datetime.now()
        self.save()
