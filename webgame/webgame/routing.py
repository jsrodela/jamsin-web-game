from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

import minesweeper.routing
import omok.routing

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webgame.settings")

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(
        URLRouter([
            *minesweeper.routing.websocket_urlpatterns,
            *omok.routing.websocket_urlpatterns,
        ])
    ))
})
