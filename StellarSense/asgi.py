"""
ASGI config for StellarSense project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# StellarSense/asgi.py

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from whitenoise import WhiteNoise  # ✅ correct import
import home.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StellarSense.settings')

# Base ASGI Django application
django_asgi_app = get_asgi_application()

# Wrap HTTP layer with WhiteNoise to serve static files
django_asgi_app = WhiteNoise(django_asgi_app, root=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles'))

# Main ASGI application with WebSocket support
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            home.routing.websocket_urlpatterns
        )
    ),
})
