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


# Captcha
RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
# RECAPTCHA_PROXY = {'http': 'http://127.0.0.1:8000', 'https': 'https://127.0.0.1:8000'}
# RECAPTCHA_DOMAIN = 'www.recaptcha.net'
RECAPTCHA_DOMAIN = 'www.google.net'
RECAPTCHA_REQUIRED_SCORE = 0.85
