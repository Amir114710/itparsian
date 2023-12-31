from os import path
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%^q9=f&^(z!znbm39!u+g^1-lcrqmk9cqo!)&@#dj@+tnyj5o4'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_PACKAGES = [
    'star_ratings',
    'widget_tweaks',
    'crispy_forms',
    'django_gravatar',
    'extensions',
    'ckeditor',
    'ckeditor_uploader',
]

MY_APPS = [
    'apps.account.apps.AccountConfig',
    'apps.blog.apps.BlogConfig',
    'apps.mysite.apps.MysiteConfig',
    'apps.ticket.apps.TicketConfig',
]
INSTALLED_APPS = [
    'admin_persian',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    *INSTALLED_PACKAGES,  # INSTALLED THIRD_PARTY_PACKAGES
    *MY_APPS,  # INSTALLED LOCAL APPS
]

MY_MIDDLEWARE = [
    'apps.blog.middleware.SaveIpMiddleware',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    *MY_MIDDLEWARE,  # MY CUSTOM MIDDLEWARE
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR , 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "context_processors.context_processors.query",
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


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

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [path.join(BASE_DIR , 'assets')] 
MEDIA_URL = 'media/'
MEDIA_ROOT = path.join(BASE_DIR , 'media')
CKEDITOR_UPLOAD_PATH = 'uploadFiles'


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Advanced',
    },
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'account.User'

STAR_RATINGS_STAR_HEIGHT = 17
STAR_RATINGS_RERATE = True
STAR_RATINGS_ANONYMOUS = True