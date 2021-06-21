# chat/routing.py
from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path('derby/', consumers.ChatConsumer.as_asgi()),
]