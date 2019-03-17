"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from . import django_logging


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO__SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.getenv('DJANGO__ENV') == "PRODUCTION" else True

# IP settings.
LOCAL_IP = os.getenv('LOCAL_IP')
DEBUG_TOOLBAR_IP = os.getenv('DJANGO__DEBUG_TOOLBAR_IP')
ALLOWED_HOSTS = [LOCAL_IP, ]
INTERNAL_IPS = [DEBUG_TOOLBAR_IP, LOCAL_IP, ]


# Application definition

INSTALLED_APPS = [
    # -- Default --
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # -- Plugins --
    # https://github.com/owais/django-webpack-loader
    # https://django-debug-toolbar.readthedocs.io/en/latest/index.html
    # https://django-otp-official.readthedocs.io/en/latest/overview.html#installation
    'webpack_loader',
    'debug_toolbar',
    'django_otp',
    'django_otp.plugins.otp_totp',
    # -- Personal --
    'home',
    'dbtasks',
]

MIDDLEWARE = [
    # -- Plugin --
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # -- Default --
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # -- Puglin --
    # https://django-otp-official.readthedocs.io/en/latest/overview.html#installation
    'django_otp.middleware.OTPMiddleware',
    # -- Default --
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # -- Default --
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # -- Personal --
                'main.context_processors.from_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DATABASE__NAME"),
        'USER': os.getenv("DATABASE__USER"),
        'PASSWORD': os.getenv("DATABASE__PASSWORD"),
        'HOST': os.getenv("DATABASE__HOST"),
        'PORT': os.getenv("DATABASE__PORT")
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ADMIN_PATH = os.getenv('STATIC_ADMIN_PATH')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)


# Trick for local https
# https://www.miximum.fr/blog/configurer-https-site-nginx-django/

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# local https next
# https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


#  Django-webpack
#  https://github.com/owais/django-webpack-loader

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}


# Logging config
# https://docs.djangoproject.com/en/2.1/topics/logging/#examples

LOGGING = django_logging.set_logging()


# Redis cache config
# https://realpython.com/caching-in-django-with-redis/
# https://docs.djangoproject.com/fr/2.1/topics/cache/#cache-key-prefixing

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "django"
    }
}
# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15


# Admin improvements
# https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8

ENVIRONMENT_NAME = os.getenv("DJANGO__ENV")
ENVIRONMENT_COLOR = os.getenv("DJANGO__ENV_COLOR", 'black')

# Django-otp settings
# https://django-otp-official.readthedocs.io/en/latest/overview.html#installation

OTP_TOTP_ISSUER = 'La crèche Humaniste.'

# Email settings
# https://docs.djangoproject.com/en/2.1/topics/email/

# DEFAULT_FROM_EMAIL=''
# SERVER_EMAIL=''
# ADMINS=''
# MANAGERS=''
