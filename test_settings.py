
INSTALLED_APPS = ('after_response',)
SECRET_KEY = 'secret'
ROOT_URLCONF = 'test_urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'after_response.signals': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
