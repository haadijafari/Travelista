from .settings import *

ALLOWED_HOSTS = [
    '127.0.0.1'
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}