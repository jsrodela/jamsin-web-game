from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/omok/', consumers.OmokConsumer.as_asgi()),
]
