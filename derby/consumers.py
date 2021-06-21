import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from derby.models import Derby


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': await self.get_db()
        }))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        #text_data_json = json.loads(text_data)
        message = text_data
        await self.send(text_data=json.dumps({
            'message': await self.get_db()
        }))

    @database_sync_to_async
    def get_db(self):
        return Derby.objects.all()[0].name
