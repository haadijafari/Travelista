from .settings import *

ALLOWED_HOSTS = [
    'example.com'
]

# Database
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'Name',
       'USER': 'User',
       'PASSWORD': 'Password',
       'HOST': 'localhost',
       'PORT': '3306',
   }
}

# Static and Media files Directory
STATIC_ROOT = 'home/$USER/public_html/static_cdn'
MEDIA_ROOT = 'home/$USER/public_html/media_cdn'
