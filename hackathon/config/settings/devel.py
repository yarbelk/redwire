from hackathon.config.settings.common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

MEDIA_URL = "http://127.0.0.1:8000/media/"

#LOGGING['loggers']['django.apps']['level'] = 'INFO'

FIXTURE_DIRS = (
        # Testing fixtures here
        )

SESSION_COOKIE_SECURE = False

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = SITE_ROOT / 'tmp/emails'  # change this to a proper location

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += ('django.contrib.webdesign',
                   'debug_toolbar',)

dbfile = SITE_ROOT / 'db' / 'devel.sqlite3'

# disabled b/c probably need GIS from postGIS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': dbfile,                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS' : False,
        }
