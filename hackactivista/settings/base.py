"""
Django settings for hackactivista project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#Para subir arvhivos multimia que pesan mas de 1Mg desde el cliente, campos de tipo: FileField o ImageField
FILE_UPLOAD_PERMISSIONS = 0o644

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'martor',
    'applications.users',
    'applications.seo',
    'applications.covid19',
    'applications.configurations'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hackactivista.urls'

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

WSGI_APPLICATION = 'hackactivista.wsgi.application'

# MODIFICANDO EL SETTIING
AUTH_USER_MODEL = 'users.Usuario'

# para login y de paso reutilizaremos para autenticacion con redes sociales
LOGIN_URL = 'iniciar_sesion'  # estamos llamando por su nombre del Url no por su URL
LOGOUT_URL = 'cerrar_sesion'
LOGIN_REDIRECT_URL = 'index_principal'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_URL = '/static/'

# esto al parecer es importane pero al momento todo funciona bien
# en cado de generar o copiar a otro directorio lo habilitamos esto con
# ./manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')

# MEDIA_ROOT = '/home/alejandro/sicoas/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
MEDIA_URL = '/media/'

# DATETIME_FORMAT = '%m/%d/%Y %H:%M:%S'
DATETIME_FORMAT = '%m/%d/%Y %I:%M'

SUIT_CONFIG = {
    'ADMIN_NAME': 'ADMINISTRADOR - Hackactivista',
    'HEADER_DATE_FORMAT': 'l, j. F Y',  # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'H:i',  # 18:42
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'MENU_OPEN_FIRST_CHILD': True,
    # falta algo, para buscar un cierto usuario
    # 'SEARCH_URL': '/administrador/usuarios/',
}
