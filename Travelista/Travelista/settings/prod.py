from .settings import *

ALLOWED_HOSTS = [
    'hadijafari.info',
    'haadijafari.ir',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['SQL_NAME'],
        'USER': os.environ['SQL_USER'],
        'PASSWORD': os.environ['SQL_PASS'],
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

# Static and Media files Directory
STATIC_ROOT = '/home/haadija1/public_html/Travelista/static'
MEDIA_ROOT = '/home/haadija1/public_html/Travelista/media'
STATIC_URL = 'Travelista/static/'
MEDIA_URL = '/Travelista/media/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Captcha
RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY_V2']
RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY_V2']
# RECAPTCHA_PROXY = {'http': 'http://127.0.0.1:8000', 'https': 'https://127.0.0.1:8000'}
# RECAPTCHA_DOMAIN = 'www.recaptcha.net'
RECAPTCHA_DOMAIN = 'www.google.net'
RECAPTCHA_REQUIRED_SCORE = 0.85

CSRF_COOKIE_SECURE = True #to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True #to avoid transmitting the session cookie over HTTP accidentally.

SECURE_HSTS_SECONDS = 15780000  # 6 Months as Recommended
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_SSL_REDIRECT = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

CSP_DEFAULT_SRC = ("'self'", "https://www.recaptcha.net", 'https://google.com')
CSP_SCRIPT_SRC = ("'self'", "https://www.recaptcha.net", "https://www.gstatic.com", "https://www.google.com", "'unsafe-inline'")
CSP_FRAME_SRC = ("'self'", "https://www.recaptcha.net", "https://www.google.com")
CSP_STYLE_SRC = ("'self'", "https://stackpath.bootstrapcdn.com", "https://www.recaptcha.net", "https://google.com", "'unsafe-inline'")
