from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/minesweeper/', consumers.MinesweeperConsumer.as_asgi()),
]
