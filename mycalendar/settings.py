"""
Django settings for mycalendar project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry import trace
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#^a095n96qp0demcyty4*=57!p5owx#1s8+dy+ix5yi05#er16'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

import logging

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logfile.log',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'husakmaria74@gmail.com'
EMAIL_HOST_PASSWORD = 'gzns kvwo aglb hkhk'
DEFAULT_FROM_EMAIL = 'husakmaria74@gmail.com'




ALLOWED_HOSTS = ['marycalendar.azurewebsites.net', 'localhost', '127.0.0.1', '*']

CSRF_TRUSTED_ORIGINS = ['https://marycalendar.azurewebsites.net']


# Application definition



INSTALLED_APPS = [
    'main',
    'mycalendar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]


SOCIALACCOUNT_LOGIN_ON_GET=True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'mycalendar.middleware.TracingMiddleware'
]

ROOT_URLCONF = 'mycalendar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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



WSGI_APPLICATION = 'mycalendar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

import environ
import sys

environ.Env.DB_SCHEMES['mssql'] = 'mssql'
env = environ.Env(DEBUG=(bool,False))
DEFAULT_DATABASE_URL = 'mssql://mariia:samsungA6.@mycalendar.database.windows.net/mycalendar?driver=ODBC+Driver+17+for+SQL+Server'

DATABASE_URL = os.environ.get('DATABASE_URL', DEFAULT_DATABASE_URL)
os.environ['DJANGO_DATABASE_URL'] = DATABASE_URL.format(**os.environ)

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    DATABASES = {
        'default': env.db('DJANGO_DATABASE_URL', default=DEFAULT_DATABASE_URL)
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / "main",
]

SITE_ID = 2

LOGIN_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}



AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend'
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

exporter = AzureMonitorTraceExporter(connection_string="InstrumentationKey=5ba07293-a0c1-4ba6-a705-2067166f6e42;IngestionEndpoint=https://northeurope-2.in.applicationinsights.azure.com/;LiveEndpoint=https://northeurope.livediagnostics.monitor.azure.com/;ApplicationId=ebf58740-15a1-447c-9ec7-0eb2faa49e6e")

tracer_provider = TracerProvider(resource=Resource.create({}),)
tracer_provider.add_span_processor(BatchSpanProcessor(exporter))

DjangoInstrumentor().instrument()
LoggingInstrumentor().instrument()
trace.set_tracer_provider(tracer_provider)
