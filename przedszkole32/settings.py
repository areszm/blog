#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Django settings for przedszkole32 project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# a setting to determine whether we are running on OpenShift
ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True
if os.environ.has_key('OPENSHIFT_APP_NAME'):
    DB_NAME = os.environ['OPENSHIFT_APP_NAME']
if os.environ.has_key('OPENSHIFT_DB_USERNAME'):
    DB_USER = os.environ['OPENSHIFT_DB_USERNAME']
if os.environ.has_key('OPENSHIFT_DB_PASSWORD'):
    DB_PASSWD = os.environ['OPENSHIFT_DB_PASSWORD']
if os.environ.has_key('OPENSHIFT_DB_HOST'):
    DB_HOST = os.environ['OPENSHIFT_DB_HOST']
if os.environ.has_key('OPENSHIFT_DB_PORT'):
    DB_PORT = os.environ['OPENSHIFT_DB_PORT']

ON_BPI = False
if os.environ.has_key('BPI_REPO_DIR'):
    ON_BPI = True
if os.environ.has_key('BPI_APP_NAME'):
    DB_NAME = os.environ['BPI_APP_NAME']
if os.environ.has_key('BPI_DB_USERNAME'):
    DB_USER = os.environ['BPI_DB_USERNAME']
if os.environ.has_key('BPI_DB_PASSWORD'):
    DB_PASSWD = os.environ['BPI_DB_PASSWORD']
if os.environ.has_key('BPI_DB_HOST'):
    DB_HOST = os.environ['BPI_DB_HOST']
if os.environ.has_key('BPI_DB_PORT'):
    DB_PORT = os.environ['BPI_DB_PORT']


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dosq1iq*$-6(uuo39e_hrqmf$j))+y%ia_!bnw7efzm9gn$9dx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SESSION_EXPIRE_AT_BROWSER_CLOSE=True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
#    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
#    'django_modalview',
    'jquery',
    'blog',
    'cookielaw',
#    'django_uwsgi',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'raven.contrib.django.raven_compat',
]

ROOT_URLCONF = 'przedszkole32.urls'

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

WSGI_APPLICATION = 'przedszkole32.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if ON_OPENSHIFT or ON_BPI:
    # os.environ['OPENSHIFT_DB_*'] variables can be used with databases created
    # with rhc app cartridge add (see /README in this git repo)
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWD,
        'HOST': DB_HOST,   # Or an IP Address that your DB is hosted on
        'PORT': DB_PORT,
        }
    }
else:
    DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'przedszkole32',
#        'USER': 'przedszkole32',
#        'PASSWORD': 'Przedszkole32',
#        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#        'PORT': '3306',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'public')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
#    os.path.join(BASE_DIR, 'public', 'static'),
#    os.path.join(DJ_PROJECT_DIR, 'static'),
)
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "$project/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
LOGIN_REDIRECT_URL = '/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
STATIC_FINDERS= STATICFILES_FINDERS
