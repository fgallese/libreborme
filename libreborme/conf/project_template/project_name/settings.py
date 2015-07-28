import os
from mongoengine import connect
from django.conf import settings


# ------ BEGIN DON'T TOUCH AREA ------ #

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = '{{ secret_key }}'

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# ------ END DON'T TOUCH AREA ------ #


DEBUG = True
DOMAIN = '<domain>'
SUBDIR = '/'  # edit this line if you are installing in a sub directory, like /libreborme
SITE_NAME = '{{ project_name }}'  # site name, you can change this

MONGO_DBNAME = 'libreborme'
MONGODB = connect(MONGO_DBNAME)

# import the default libreborme settings
# do not move this import
#from libreborme.conf.settings import *
from libreborme.settings import *


# ------ All settings customizations must go here ------ #


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

ADMINS = (
    #('Your name', 'your@email.com'),
)

MANAGERS = ADMINS

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'root@localhost'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER  # used for error reporting

STATIC_ROOT = '%s/static/' % SITE_ROOT

PIWIK_URL = ''
PIWIK_SITE_ID = ''

PROTOCOL = 'http' if DEBUG else 'https'
PORT = getattr(settings, 'PORT', '8000') if DEBUG else None

if PORT and str(PORT) not in ['80', '443']:
    PORT_STRING = ':%s' % PORT
else:
    PORT_STRING = ''

SUBDIR = getattr(settings, 'SUBDIR', '')

if SUBDIR and not SUBDIR.startswith('/'):
    SUBDIR = '/%s' % SUBDIR
elif SUBDIR and SUBDIR.endswith('/'):
    SUBDIR = SUBDIR[0:-1]

SITE_URL = '%s://%s%s%s' % (PROTOCOL, settings.DOMAIN, PORT_STRING, SUBDIR)

MEDIA_URL = '%s/media/' % SITE_URL
MEDIA_ROOT = '%s/media/' % SITE_ROOT
STATIC_ROOT = '%s/static/' % SITE_ROOT

# BORME
BORME_PDF_ROOT = '%s/borme/pdf/' % SITE_ROOT
BORME_PDF_TEMP_ROOT = '%s/borme/pdf/tmp/' % SITE_ROOT
BORME_XML_ROOT = '%s/borme/xml/' % SITE_ROOT
