"""
Django settings for ben project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lla&nz(w@863d#p=xf$*k^^rqfb@u^%u94=+@7%g+*w_-gn%=j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['kellyb45.pythonanywhere.com', 'localhost', 'localhost:8000', '0.0.0.0', '127.0.0.1', '172.31.0.0', '136.206.203.76', 'smartpredict.ckvcd6jodx0m.eu-west-1.rds.amazonaws.com']


# Application definition

INSTALLED_APPS = [
    'smartpredict.apps.SmartpredictConfig',
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
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'bootstrap3',
    'oauth2_provider',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # If you use SessionAuthenticationMiddleware, be sure it appears before OAuth2TokenMiddleware.
    # SessionAuthenticationMiddleware is NOT required for using django-oauth-toolkit.
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'ben.urls'

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


WSGI_APPLICATION = 'ben.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

#if 'smartpredict' in os.environ:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#else:
#   DATABASES = {
#       'default': {
#           'ENGINE': 'django.db.backends.mysql',
#            'NAME': os.environ['smartpredict'],
#            'USER': os.environ['kellyb45'],
#            'PASSWORD': os.environ[''],
#            'HOST': os.environ['smartpredict.ckvcd6jodx0m.eu-west-1.rds.amazonaws.com'],
#            'PORT': os.environ['3306'],
#        }
#    }

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'smartpredict',
#        'USER': 'kellyb45',
#        'PASSWORD': 'xxxx',
#        'HOST': 'smartpredict.ckvcd6jodx0m.eu-west-1.rds.amazonaws.com',
#        'PORT': '3306',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
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
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1019465027563-bs5923ifa3nf6ipkeintfcrtfoulq06b.apps.googleusercontent.com'
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'TxDbuYhiIgPztLpT0nzx9aum'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True



EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    # Uncomment following if you want to access the admin
    #'django.contrib.auth.backends.ModelBackend'
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

#AUTH_USER_MODEL = `users.CustomUser`

SITE_ID = 1
#MEDIA_URL = '/media/'
REGISTER_REDIRECT_URL = '/smartpredict'
LOGIN_REDIRECT_URL = '/smartpredict'
LOGOUT_REDIRECT_URL = '/smartpredict'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
#http://kellyb45.pythonanywhere.com/user/kellyb45/files/home/kellyb45/2019-ca400-kellyb45/src/static/smartpredict/logo.png
#https://www.pythonanywhere.com/user/kellyb45/files/home/kellyb45/2019-ca400-kellyb45/src/static/smartpredict/logo.png