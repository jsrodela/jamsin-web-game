from channels.generic.websocket import WebsocketConsumer


class OmokConsumer(WebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        pass
