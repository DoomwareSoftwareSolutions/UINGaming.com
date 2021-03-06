from django.utils.translation import ugettext as _
# Django settings for WebApp project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('tomas','tomasboccardo@gmail.com')
	# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'UINGaming',                     # Or path to database file if using sqlite3.
		# The following settings are not used with sqlite3:
		'USER': 'admin',
		'PASSWORD': 'admin',
		'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
		'PORT': '',                      # Set to empty string for default.
	}
}

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
		'LOCATION': '127.0.0.1:11211',
	}
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	'/home/user/Desktop/UINGaming.com/UINGaming/static',
	'/home/fede/Desktop/UINGaming.com/UINGaming/static',
	'/home/tomas/workspace/UINGaming.com/UINGaming/static',
	'/home/tboccardo/workspace/UINGaming.com/UINGaming/static',
	'/home/federico/Escritorio/UINGaming.com/UINGaming/static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'rktb*sd*v+v*@st0#v#$l65=0n_6r86^jp)da8@24w^=a@to5=' #THIS IS DEBUG CONFIG

# Password hashing algorithm. Posible values: 'SHA256', 'BCRYPT' , 'NONE'
CRYPT_ALGORITHM='SHA256'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.locale.LocaleMiddleware'
	# Uncomment the next line for simple clickjacking protection:
	# 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'UINGaming.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'UINGaming.wsgi.application'

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	'/home/user/Desktop/UINGaming.com/UINGaming/templates',
	'/home/fede/Desktop/UINGaming.com/UINGaming/templates',
	'/home/tomas/workspace/UINGaming.com/UINGaming/templates',
	'/home/tboccardo/workspace/UINGaming.com/UINGaming/templates',
	'/home/federico/Escritorio/UINGaming.com/UINGaming/templates',
)

SOUTH_TESTS_MIGRATE = False

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',
	'src.users',
	'src.events',
	'src.home',
	'south'
)

# Email Configuration
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #PARA PODER USAR LA TESTING ADDRESS
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #PARA IMPRIMIR MAILS POR CONSOLA

TESTING_ADDRESS = 'doomwaresoftsol@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'doomwaresoftsol@gmail.com'
EMAIL_HOST_PASSWORD = '' #Por cuestiones de seguridad esto no sera subido al repo
EMAIL_SUBJECT_PREFIX = '[UINGAMING]'
EMAIL_USE_TLS = True

NOREPLY_ADDRESS = 'noreply@uingaming.com'
INFO_ADDRESS = 'info@uingaming.com'

PASSWORD_RECOVERY_URL= 'http://localhost:8000/password_recover/'

LOCALE_PATHS = (
	'/home/fede/Desktop/UINGaming.com/UINGaming/locale',
)

LANGUAGES = (
  ('es', _('Spanish')),
  ('en', _('English')),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}
