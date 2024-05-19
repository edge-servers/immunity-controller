from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'immunity22',
        'USER': 'immunity22',
        'PASSWORD': 'immunity22',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}
