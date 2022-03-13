from pathlib import Path

from datetime import timedelta

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)                  # cast=bool vannale convert string to boolean value vaneko

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authentication.apps.AuthenticationConfig',     # for authentication app
    'orders.apps.OrdersConfig',                     # for orders app        

    'rest_framework',                               # pip install djangorestframework


    'djoser',                                       # pip install djoser

    'phonenumber_field',                            # pip install django-phonenumber-field[phonenumbers]


    'drf_yasg',                                     # pip install drf-yasg   for the swagger UI in django
]


AUTH_USER_MODEL = 'authentication.User'              # 'authentication.User' vannale, since we are using custom user model, so tei vayera authentication app ko User class nai hamro custom user model ho vanera chinayeko

REST_FRAMEWORK = {

    "NON_FIELD_ERRORS_KEY": "error",                # non_field_errors lai just error matra dislplay garauna ko lagi

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',        # for djangorestframework-simplejwt package
    )

}


SIMPLE_JWT = {

    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),         # Generally access token always has shorter life span than the Refresh Token    # project develop garda kheri access token to time seconds ma rakhera test garna parcha, because error cha ki nai ramro sanga herna sakincha
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),           # we use the Refresh Token to frequently update the access token after certain time.    # Refresh token has larger life span.

    'ROTATE_REFRESH_TOKENS': True,                          # Rotate Refresh Token lai True gareko because when the refresh token expires user doesn't have to login again... i.e automatically new refresh token and access token generate garos vanera.  
    
    # 'BLACKLIST_AFTER_ROTATION': True,                     # access token expire vayera feri naya refresh token generate gare pachi.. pahila ko old refresh token lai blacklist garna parcha natra vane jasle pani tyo pahilako(old) refresh token ko help batw access token generate garna sakcha so yesto nahos vanna ko lagi tyo pahila ko(old) refresh token lai balcklist garna ko lagi True garkeo ho.
    'BLACKLIST_AFTER_ROTATION': False,                      # Khas ma yo True nai gareko secure huncha, but auta error tackle garna nasakera False gareko ho                 

    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),                       # AUTH_HEADER_TYPES default ma JWT huncha, teslai BEARER garayeko
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


SWAGGER_SETTINGS = {                # Swagger Configurations

    'SECURITY_DEFINITIONS':{
        'Bearer':{
            'type':'apiKey',
            'in':'header',
            'name':'Authorization'
        }
    }

}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'momo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'momo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
        'init_command': 'SET foreign_key_checks = 0;',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
