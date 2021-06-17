"""
Django settings for Django1 project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import mimetypes
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# from celery.schedules import crontab
from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG_MODE') == "1"
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(":")
# Celery configuration
# CELERY_BROKER_URL = 'amqp://localhost'

CELERY_BROKER_URL = 'amqp://{0}:{1}@{2}:5672'.format(
    os.environ.get('RABBITMQ_DEFAULT_USER', "guest"),
    os.environ.get('RABBITMQ_DEFAULT_PASS', "guest"),
    os.environ.get('RABBITMQ_DEFAULT_HOST', "localhost"),
)
print(CELERY_BROKER_URL)

CELERY_TIMEZONE = "Europe/Kiev"
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BEAT_SCHEDULE = {
    "delete_logs": {
        "task": "main.task.delete_logs",
        "schedule": crontab(minute="0", hour="1")

    },
    "mail_send_9am": {
        "task": "main.task.mail_send_9am",
        "schedule": crontab(minute="0", hour="9")
    }
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'debug_toolbar',
    'django_extensions',
    "bootstrap4",
    'account',
    'main',
    'rest_framework',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'main.middleware.SimpleMiddleware',
    'main.middleware.LogMiddleware',
    # 'main.middleware.MetricsMiddleware',
]

ROOT_URLCONF = 'Django1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Django1.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_ssb',
#         'USER': 'postgres',
#         'PASSWORD': 'ssb',
#         'HOST': '127.0.0.1',
#         'PORT': '',
#     }
# }

# CACHED

CACHE = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

mimetypes.add_type("text/css", ".css", True)
# mimetypes.add_type("text/html", ".css", True)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


# RunServer
# STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static_content', 'static')

#Docker
STATIC_ROOT = os.path.join('/tmp', 'static_content', 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_content')

# AUTH CONFIGURATION
AUTH_USER_MODEL = 'account.user'

# TELEGRAM_BOT_API = "bot122456789"

INTERNAL_IPS = [
    '127.0.0.1',
    '0.0.0.0'
]

if DEBUG:
    import socket

    DEBUG_TOOLBAR_PATCH_SETTINGS = True

    INTERNAL_IPS = [socket.gethostbyname(socket.gethostname())[:-1] + '1']

LOGIN_REDIRECT_URL = '/'
REDIRECT_FIELD_NAME = '/'
