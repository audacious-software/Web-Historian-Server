from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'CHANGEMECHANGEMECHANGEMECHANGEMECHANGEMECHANGEMECHANGEMECHANGEME' # nosec
DEBUG = False

ALLOWED_HOSTS = ['webhistorian.example.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME':     'circle_test',
        'USER':     'root',
        'PASSWORD': '', # nosec
        'HOST': 'localhost',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR) + '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR) + '/media/'

TIME_ZONE = 'America/Chicago'

SITE_URL = 'https://%s' % ALLOWED_HOSTS[0]
