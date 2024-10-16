from pathlib import Path
import os
from dotenv import load_dotenv


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv('DEBUG', default=False)
DEBUG = True


ALLOWED_HOSTS = ['www.gitapp.bilalahmed.dev', 'gitapp.bilalahmed.dev', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local Apps
    "portfolio_api",
    "file_convert",
    # Thirt Party Apps
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            str(BASE_DIR.joinpath('Portfolio_front_app')),
        ],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'

# print("hostname ", os.environ.get("PORTFOLIO_DB_HOST"))
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        # 'ENGINE': 'mysql.connector.django',
        # 'NAME': 'uihxzefkgh_portfolio',
        # 'USER': 'uihxzefkgh_admin',
        # 'PASSWORD': 'IhqYAj)+XRRJ',
        # 'HOST': '120.0.0.1',
        # 'PORT': 3306,

        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.environ.get("PORTFOLIO_DB_NAME"),
        # 'USER': os.environ.get("PORTFOLIO_DB_USER"),
        # 'PASSWORD': os.environ.get("PORTFOLIO_DB_PASSWORD"),
        # 'HOST': os.environ.get("PORTFOLIO_DB_HOST"),
        # 'PORT': os.environ.get("PORTFOLIO_DB_PORT"),
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# *ic files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

# static root for hosting file directory
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
MEDIA_ROOT = str(BASE_DIR.joinpath("media"))

if DEBUG:
    STATICFILES_DIRS = [
        str(BASE_DIR.joinpath('Portfolio_front_app/static')),  # for APP6 FRONTEND
        str(BASE_DIR.joinpath('static')),
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://localhost:3000',
    # str(os.getenv('CORS_ALLOWED_ORIGINS_API')),
]

REST_FRAMEWORK = {
    # Testing api format
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    # Json Format
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    # ],
}
