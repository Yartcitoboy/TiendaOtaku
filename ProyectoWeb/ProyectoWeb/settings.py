"""
Django settings for ProyectoWeb project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from django.urls import reverse_lazy
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-06x-5un7p87_y*k!xi9%%uyevke$)kmfseviu%-ii%+e^s*2wu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#ESTO ES NO LE PRESTE MUCHA ATENCION YA QUE ESTO NO ES MATERIA QUE VIMOS, ES ALGO PARA VERIFICAR SI EXISTE UNA CUENTA PARA LOGUEARTE EN LA PAGINA
LOGIN_REDIRECT_URL = reverse_lazy ('index')
LOGOUT_REDIRECT_URL = reverse_lazy('login')


# Application definition

INSTALLED_APPS = [
    'crispy_forms', #esto es para un formulario personalizado dentro de Django
    'crispy_bootstrap5',#esto igual que ariba
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'OtakuShop.apps.OtakushopConfig' # esto se agrega cuando agregas una aplicacion en el cmd cuadno creas el proyecto.
    
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
# lo de arriba y abajo va con lo de crispy 
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProyectoWeb.urls'

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

WSGI_APPLICATION = 'ProyectoWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#SOLAMENTE USAMOS DJANGO APRA LA BASE DE DATOS, SI QUIERES PUEDES USAR EL DE ORACLE, DEBES COMENTAR LO DE DJANDO DE DEJA EL ORACLE SIN COMENTAR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.oracle',
    #     'NAME': 'localhost/xe',
    #     'USER': 'TiendaOtaku',
    #     'PASSWORD': 'TiendaOtaku',
    #     'TEST': {
    #         'USER': 'default_test',
    #         'TBLSPACE': 'default_test_tbls',
    #         'TBLSPACE_TMP': 'default_test_tbls_tmp',
    #     },
    # },
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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/



STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


