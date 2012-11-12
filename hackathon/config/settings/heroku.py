from common import *
import dj_database_url
import os

DATABASES = {'default': 
        dj_database_url.config(default=os.environ['HEROKU_POSTGRESQL_OLIVE_URL']),
        }
