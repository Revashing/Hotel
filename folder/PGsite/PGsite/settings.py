"""
Django settings for PGsite project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv
from django.core.exceptions import ValidationError

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
	'PGapp',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.postgres',
	'django.contrib.sites',
	'django_extensions',
	'crispy_forms',
	'django_cleanup',
	'easy_thumbnails',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.google',
	'allauth.socialaccount.providers.github',
	'allauth.socialaccount.providers.facebook',
	'allauth.socialaccount.providers.yandex',
	]

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	]

ROOT_URLCONF = 'PGsite.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'templates'),
			os.path.join(BASE_DIR, 'PGapp', 'templates', 'PGapp'),
			],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.request',
				],
			},
		},
	]

WSGI_APPLICATION = 'PGsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": os.environ.get("SQL_ENGINE"),
		"NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
		"USER": os.environ.get("SQL_USER", "user"),
		"PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
		"HOST": os.environ.get("SQL_HOST", "localhost"),
		"PORT": os.environ.get("SQL_PORT", "5432"),
		}
	}

SOCIALACCOUNT_PROVIDERS = {
	'google': {
		'SCOPE': [
			'profile',
			'email',
			],
		'AUTH_PARAMS': {
			'access_type': 'online',
			},
		'OAUTH_PKCE_ENABLED': True,
		}
	}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
		'OPTIONS': {
			'max_similarity': 0.5,
			},
		},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
		'OPTIONS': {
			'min_length': 11,
			},
		},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
		},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
		},
	{
		'NAME': 'NoForbiddenCharsValidator',
		'OPTIONS': {
			'forbidden_chars': (' ', ',', ', ', '.', ':', ';'),
			},
		},
	]


# CUSTOM VALIDATION

class NoForbiddenCharsValidator:
	def __init__(self, forbidden_chars=(' ',)):
		self.forbidden_chars = forbidden_chars

	def validate(self, password, user=None):
		for forbidden_char in self.forbidden_chars:
			if forbidden_char in password:
				raise ValidationError(
					'Password must not contain forbidden characters %s'%', '.join(self.forbidden_chars),
					code='forbidden_chars_present'
					)

	def get_help_text(self):
		return 'Password must not contain forbidden characters %s'%', '.join(self.forbidden_chars)


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_TZ = True

DATE_INPUT_FORMATS = ['%d-%m-%Y']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

THUMBNAIL_ALIASES = {
	'PGapp.HotelRooms.picture': {
		'default': {
			'size': {400, 300},
			'crop': 'scale',
			},
		},
	}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BOOTSTRAP4 = {
	'required_css_class': 'required',
	'success_css_class': 'has_success',
	'error_css_class': 'has_error',

	'horizontal_field_class': '',
	'horizontal_error_class': '',
	}

AUTHENTICATION_BACKENDS = [
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
	]

LOGIN_URL = 'PGapp:login'
LOGIN_REDIRECT_URL = 'PGapp:start_page'
ACCOUNT_LOGOUT_REDIRECT_URL = 'PGapp:login'
PASSWORD_RESET_TIMEOUT_DAYS = 3

