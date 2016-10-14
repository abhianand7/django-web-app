"""
Django settings for recepieweb project.

Generated by 'django-admin startproject' using Django 1.9.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '5m!9(m#yy=m%-3bt%^m&8et98-l2$ba1h3h$dnot=m72j_52p4'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.instagram',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
    'djangocms_text_ckeditor',
    'treebeard',
    'menus',
    'sekizai',
    'easy_thumbnails',
    'filer',
    # 'mptt' to be included as a must feature as this increases the fetching of data from databases
    'cmsplugin_filer_utils',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'norecepieweb',
]

SITE_ID = 1

# for supporting retina displays, like MacBooks
THUMBNAIL_HIGH_RESOLUTION = True

MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
    ],
    'skin': 'moono',
}


ADMINS = [('Abhinav', 'erabhinav@outlook.com'), ('Jeffrey', 'jeffreylunt@gmail.com')]

# Authentication Backends
AUTHENTICATION_BACKENDS = [
                            'django.contrib.auth.backends.ModelBackend',
                            'allauth.account.auth_backends.AuthenticationBackend',
                           ]

# Whether to prepend the 'www.' sub-domain to URLs that dont have it.
PREPEND_WWW = False

# If a URL path matches a regular expression in this list, the request will not be redirected to HTTPS.
#  If SECURE_SSL_REDIRECT is False, this setting has no effect.
SECURE_REDIRECT_EXEMPT = []

# If a string (e.g. secure.example.com), all SSL redirects will be directed to
#  this host rather than the originally-requested host
# (e.g. www.example.com). If SECURE_SSL_REDIRECT is False, this setting has no effect.
# SECURE_SSL_HOST = None

# If True, the SecurityMiddleware redirects all non-HTTPS requests to HTTPS
# (except for those URLs matching a regular expression listed in SECURE_REDIRECT_EXEMPT).
SECURE_SSL_REDIRECT = False

# The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
SERVER_EMAIL = 'error@recepieweb.com'

# The backend used for signing cookies and other data.
SIGNING_BACKEND = 'django.core.signing.TimestampSigner'

# A list of identifiers of messages generated by the system check framework (i.e. ["models.W001"])
# that you wish to permanently acknowledge and ignore. Silenced checks will not be output to the console.
SILENCED_SYSTEM_CHECKS = []

# The URL where requests are redirected after login when
# the contrib.auth.login view gets no next parameter.
LOGIN_REDIRECT_URL = '/accounts/profile/'
# The URL where requests are redirected after a user logs out using the logout() view
# (if the view doesnt get a next_page argument).
LOGOUT_REDIRECT_URL = None

# Max memory upload size
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440

# Data upload max number field
# The maximum number of parameters that may be received
# via GET or POST before a SuspiciousOperation (TooManyFields) is raised.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

# database routers
# The list of routers that will be used to determine which
# database to use when performing a database query.
DATABASE_ROUTERS = []

# If set to True, Djangos normal exception handling of view functions will be suppressed,
#  and exceptions will propagate upwards.
# This can be useful for some test setups, and should never be used on a live site.
DEBUG_PROPAGATE_EXCEPTIONS = False

# Default charset to use for all HttpResponse objects,
# if a MIME type isnt manually specified.
# Used with DEFAULT_CONTENT_TYPE to construct the Content-Type header.
DEFAULT_CHARSET = 'utf-8'

# Default content type to use for all HttpResponse objects,
# if a MIME type isnt manually specified.
# Used with DEFAULT_CHARSET to construct the Content-Type header.
DEFAULT_CONTENT_TYPE = 'text/html'

# Default email address to use for various automated correspondence from the site manager(s).
# This doesnt include error messages sent to ADMINS and MANAGERS;
# for that, see SERVER_EMAIL.
DEFAULT_FROM_EMAIL = 'webmaster@recepieweb.com'

# List of compiled regular expression objects representing User-Agent strings that are not allowed to visit any page,
# system-wide. Use this for bad robots/crawlers.
# This is only used if CommonMiddleware is installed
DISALLOWED_USER_AGENTS = []


# url config file
ROOT_URLCONF = 'recepieweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'django.template.context_processors.request',
            ],
        },
    },
]

CMS_TEMPLATE = 'recepieweb.templates'

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)

WSGI_APPLICATION = 'recepieweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': 'mytestdatabase',
        },
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

LANGUAGES = [
    ('en-us', 'English'),
]
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
