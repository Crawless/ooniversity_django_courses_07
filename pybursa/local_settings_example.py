import os
from .settings import BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1w*r07-074z1uyq@wf@&il8i#k!ws^l^2ffd4df3=l)b)w8xuf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'savr11.online']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

ADMINS = [('Admin', 'example@example.com')]

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        'courses': {
            'handlers': ['file_courses'],
            'level': 'DEBUG',
        },
        'students': {
            'handlers': ['file_students'],
            'level': 'WARNING',
        },
    },
    'handlers': {
        'file_courses': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
            'formatter': 'simple',
        },
        'file_students': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
            'formatter': 'verbose',
        },
    },
}