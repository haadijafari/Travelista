"""
WSGI config for Travelista project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from Travelista.settings.settings import DEBUG

from django.core.wsgi import get_wsgi_application

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Travelista.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Travelista.settings.prod')

application = get_wsgi_application()
