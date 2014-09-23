# -*- coding: utf-8 -*-
"""Django settings for django-plainpasswordhasher demo project."""
import os


# Configure some relative directories.
demoproject_dir = os.path.dirname(os.path.abspath(__file__))
demo_dir = os.path.dirname(demoproject_dir)
root_dir = os.path.dirname(demo_dir)
data_dir = os.path.join(root_dir, 'var')
cfg_dir = os.path.join(root_dir, 'etc')


# Mandatory settings.
ROOT_URLCONF = '{package}.urls'.format(package=__package__)
WSGI_APPLICATION = '{package}.wsgi.application'.format(package=__package__)


# Database.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(data_dir, 'db.sqlite'),
    }
}


# Required.
SECRET_KEY = "This is a secret made public on project's repository."

# Media and static files.
MEDIA_ROOT = os.path.join(data_dir, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(data_dir, 'static')
STATIC_URL = '/static/'


# Applications.
INSTALLED_APPS = (
    # The actual demo.
    'django_plainpasswordhasher_demo',
    'django_plainpasswordhasher',
    # Third-parties.
    'south',
    # Standard Django applications.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Stuff that must be at the end.
    'django_nose',
)


# Test/development settings.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
nose_cfg_dir = os.path.join(cfg_dir, 'nose')
NOSE_ARGS = [
    '--verbosity=2',
    '--no-path-adjustment',
    '--nocapture',
    '--all-modules',
    '--rednose',
]
SOUTH_TESTS_MIGRATE = False


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django_dummysign': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django_anysign_demo': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django_dummysign': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
