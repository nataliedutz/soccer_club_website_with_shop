"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# Set SECRET_KEY with a default value of 'change-me'
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())

# Set DEBUG with a default value of '1' and convert it to a boolean
DEBUG = os.getenv('DEBUG', '1') == '1'

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1").split(",")

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-7v_q!)9f0v#7x^o)y8^q7%-ol=2(alr416_mivp2te-=jg*(fc"

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "team.apps.TeamConfig",
    "shop.apps.ShopConfig",
    "accounts.apps.AccountsConfig",
    "post.apps.PostConfig",
    "api.apps.ApiConfig",
    "legal.apps.LegalConfig",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, 'templates'),  
            os.path.join(BASE_DIR, 'team', 'templates'),
            os.path.join(BASE_DIR, 'authentication', 'templates'),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

POSTGRES_DB = os.getenv("POSTGRES_DB") # database name
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD") # database user password
POSTGRES_USER = os.getenv("POSTGRES_USER") # database username
POSTGRES_HOST = os.getenv("POSTGRES_HOST") # database host
POSTGRES_PORT = os.getenv("POSTGRES_PORT") # database port

POSTGRES_READY = (
    POSTGRES_DB is not None
    and POSTGRES_PASSWORD is not None
    and POSTGRES_USER is not None
    and POSTGRES_HOST is not None
    and POSTGRES_PORT is not None
)
if POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": 'django.db.backends.postgresql_psycopg2',
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USER,
            "PASSWORD": POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT": POSTGRES_PORT,
        }
    }



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ], 
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = BASE_DIR / 'static'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = 'team:home_page' 
LOGOUT_REDIRECT_URL = 'team:home_page'
LOGIN_URL = '/login/'

# Define the base directory for your project
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to the media folder
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Define the URL for serving media files
MEDIA_URL = '/media/'
