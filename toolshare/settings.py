"""
Django settings for toolshare project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    BASE_DIR + '/templates', 
)

#TEMPLATE_LOADERS = (
   # 'django.template.loaders.filesystem.Loader',
    #'django.template.loaders.app_directories.Loader',
#)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h%+$ufj)yxbdargb*$l3!&@h=(&903@9(g93%ix1co9=+u*u9p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


#site id
SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'registration',
    'profiles',
    'users',
    'sharecenter',
    'django_messages',
    'notifications',
    'borrow_requests',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'toolshare.urls'

WSGI_APPLICATION = 'toolshare.wsgi.application'


from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + \
    ('django_messages.context_processors.inbox',
        'django_messages.context_processors.inbox_preview',
        'notifications.context_processors.notifications_new_count', 
        'notifications.context_processors.notifications_new',
        'notifications.context_processors.notification_types',
        'borrow_requests.context_processors.borrow_request_status',)

# Activation time limit for new accounts
ACCOUNT_ACTIVATION_DAYS = 7

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Media files (Placed in static for development and debuging)
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media");#BASE_DIR + '/media/'
MEDIA_URL = '/media/'

# Used by profiles app
AUTH_PROFILE_MODULE = 'users.UserProfile'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'


# Display activation emails in the console ifi n debug mode
#if DEBUG:
 #   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
