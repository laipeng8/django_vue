"""
ASGI config for django_vue project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import routings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_vue.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),#会自动去urls.py去找
        "websocket": AuthMiddlewareStack(
            URLRouter(
                routings.websocket_urlpatterns
                # Add your WebSocket routing here
            ),
        ),
    }
)

