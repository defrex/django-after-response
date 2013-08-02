
INSTALLED_APPS = ('after_response',)
SECRET_KEY = 'secret'
ROOT_URLCONF = 'test_urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
