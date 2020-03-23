"""
Things that should be modified here:
*ALLOWED HOST
*INSTALLED APPS
*DATABASE SETTINGS (NAME, USER, PASSWORD, PORT, HOST)
*TEMPLATES DIRS
*STATIC DIRS
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# IMPORTANT: keep the secret key used in production secret!
SECRET_KEY = 'fe$tu-z8w$)$(5cbll$$%llqele65y%vmh_4w2j^5@)*5ur-m_'

# IMPORTANT: don't run with debug turned on in production!
DEBUG = True

# ALLOWING ALL HOSTS FOR NOW
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ADDING THE APPS THAT WE CREATED
    'Apps.Reproduccion',
    'Apps.User'
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

ROOT_URLCONF = 'spotify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # CHANGING THE PATH OF THE TEMPLATES
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

WSGI_APPLICATION = 'spotify.wsgi.application'

DATABASES = {
    'default': {
        # CHANGING THE DATABASE SETTINGS
        'ENGINE': 'django.db.backends.mysql', 
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'spotify',
        'USER': 'root',
        'PASSWORD': '',
    }
}

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

# I'VE CHANGED THE LANGUAGE AND REGION IN "LANGUAGE_CODE", SO THE SITE CAN BE IN ENGLISH
# IF YOU WANT YOU CAN MAKE THIS CHANGE ALSO. IF YOU DECIDED NOT TO, IT'S OK
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# CHANGING THE PATH FOR STATIC FILES (CSS, JS AND IMAGES)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Static"),
]