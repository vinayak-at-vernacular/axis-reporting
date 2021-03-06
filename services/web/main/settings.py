"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import cx_Oracle

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h18&imd2qy7o_r^-gy)n)go4i*3j5nfd=&1ode@fczzt=ak(dk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api'
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

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'fsm_service', #'os.path.join(BASE_DIR, 'db.sqlite3')'
    #     'HOST': os.environ.get('PGHOST', 'localhost'),
    #     'PORT': os.environ.get('PGPORT'),
    #     'USER': os.environ.get('PGUSER'),
    #     'PASSWORD': os.environ.get('PGPASSWORD'),
    # }
    'default' : {
        'ENGINE': 'django.db.backends.oracle',
	'NAME': '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=ec2-13-233-153-210.ap-south-1.compute.amazonaws.com)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=fsm_test)))',
#        'NAME': 'ec2-13-233-153-210.ap-south-1.compute.amazonaws.com:1521/fsm_test?as=sysdba', #'sys/oracle@ec2-13-233-153-210.ap-south-1.compute.amazonaws.com:1521/fsm_test?as=sysdba', #os.environ.get('ORACLE_DATABASE'),
        #'HOST': 'ec2-13-233-153-210.ap-south-1.compute.amazonaws.com', #os.environ.get('PGHOST'),
        #'PORT': 1521, #os.environ.get('PGPORT'),
        'USER': 'SYS', #os.environ.get('PGUSER'),
        'PASSWORD': 'oracle', #os.environ.get('PGPASSWORD'),
        'OPTIONS': {
            'purity': cx_Oracle.ATTR_PURITY_SELF,
            'mode': cx_Oracle.SYSDBA
        }
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
