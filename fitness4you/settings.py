"""
Django settings for fitness4you project.
Generated by 'django-admin startproject' using Django 3.0.1.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
 
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf import settings
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY', '')
# SECRET_KEY = 's'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ
print(DEBUG)
# DEBUG = True

ALLOWED_HOSTS = ['fitness4you.herokuapp.com', 'fitness4you.onrender.com','localhost', '127.0.0.1:8000', '127.0.0.1', '4d317cc4e698.ngrok.io']

# Application definition

INSTALLED_APPS = [
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
    'home',
    'products',
    'bag',
    'django_filters',
    'django_countries',
    'checkout',
    'crispy_forms',
    'crispy_forms_materialize',
    'materializecssform',
    'profiles',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fitness4you.urls'
CRISPY_TEMPLATE_PACK = 'materialize_css_forms'
# CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'bag.contexts.bag_content',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'fitness4you.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    } 

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if 'USE_CLOUDINARY' in os.environ:
    # Heroku static files with whitenoise
    STATIC_ROOT = os.path.join(BASE_DIR, "live-static", "static-root")
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # Media files with cloudinary
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'arloys',  # required
        'API_KEY': os.getenv('API_KEY', ''),  # required
        'API_SECRET': os.getenv('API_SECRET', ''),  # required
        'SECURE': True,
        'MEDIA_TAG': 'media',
        'INVALID_VIDEO_ERROR_MESSAGE': 'Please upload a valid video file.',
        'EXCLUDE_DELETE_ORPHANED_MEDIA_PATHS': (),
        'STATIC_TAG': 'static',
        'STATICFILES_MANIFEST_ROOT': os.path.join(BASE_DIR, 'manifest'),
        'STATIC_IMAGES_EXTENSIONS': ['jpg', 'jpe', 'jpeg', 'jpc', 'jp2', 'j2k', 'wdp', 'jxr',
                                     'hdp', 'png', 'gif', 'webp', 'bmp', 'tif', 'tiff', 'ico'],
        'STATIC_VIDEOS_EXTENSIONS': ['mp4', 'webm', 'flv', 'mov', 'ogv', '3gp', '3g2', 'wmv',
                                     'mpeg', 'flv', 'mkv', 'avi'],
        'MAGIC_FILE_PATH': 'magic',
        'PREFIX': settings.MEDIA_URL
    }
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'  # Where to upload

# Stripe
STRIPE_CURRENCY = 'usd'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

if 'DEVELOPMENT' not in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'arloysmaciasrojas@gmail.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

# EMAIL_BACKEND = "sgbackend.SendGridBackend"
# SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
# EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

#Super User
SU_USERNAME=os.getenv('SU_USERNAME')
SU_EMAIL=os.getenv('SU_EMAIL')
SU_PASSWORD=os.getenv('SU_PASSWORD')
