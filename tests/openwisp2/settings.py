import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TESTING = sys.argv[1:2] == ['test']
SELENIUM_HEADLESS = True if os.environ.get('SELENIUM_HEADLESS', False) else False
SHELL = 'shell' in sys.argv or 'shell_plus' in sys.argv

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'immunity_utils.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'immunity-controller.db'),
    }
}

SPATIALITE_LIBRARY_PATH = 'mod_spatialite.so'

SECRET_KEY = 'fn)t*+$)ugeyip6-#txyy$5wf2ervc0d2n#h)qb)y5@ly$t*@w'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    # all-auth
    'django.contrib.sites',
    'immunity_users.accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_extensions',
    # immunity22 modules
    'immunity_users',
    'immunity_controller.config',
    'immunity_controller.pki',
    'immunity_controller.geo',
    'immunity_controller.connection',
    'immunity_controller.subnet_division',
    'immunity_notifications',
    'immunity_ipam',
    # immunity22 admin theme
    # (must be loaded here)
    'immunity_utils.admin_theme',
    'admin_auto_filters',
    # admin
    'django.contrib.admin',
    'django.forms',
    # other dependencies
    'sortedm2m',
    'reversion',
    'leaflet',
    'flat_json_widget',
    # rest framework
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_gis',
    'django_filters',
    'drf_yasg',
    # channels
    'channels',
    'import_export',
    # 'debug_toolbar',
]
EXTENDED_APPS = ('django_x509', 'django_loci')

AUTH_USER_MODEL = 'immunity_users.User'
SITE_ID = 1

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'immunity_utils.staticfiles.DependencyFinder',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'immunity22.urls'

ASGI_APPLICATION = 'immunity22.asgi.application'
if not TESTING:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {'hosts': ['redis://localhost/7']},
        }
    }
else:
    CHANNEL_LAYERS = {'default': {'BACKEND': 'channels.layers.InMemoryChannelLayer'}}

TIME_ZONE = 'Europe/Rome'
LANGUAGE_CODE = 'en-gb'
USE_TZ = True
USE_I18N = False
USE_L10N = False
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = f'{os.path.dirname(BASE_DIR)}/media/'

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'immunity_utils.loaders.DependencyLoader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'immunity_utils.admin_theme.context_processor.menu_groups',
                'immunity_notifications.context_processors.notification_api_settings',
            ],
        },
    }
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

EMAIL_PORT = '1025'  # for testing purposes
LOGIN_REDIRECT_URL = 'admin:index'
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL
OPENWISP_ORGANIZATION_USER_ADMIN = True  # tests will fail without this setting
OPENWISP_ADMIN_DASHBOARD_ENABLED = True
OPENWISP_CONTROLLER_GROUP_PIE_CHART = True
# during development only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if not TESTING:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/6',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
        }
    }

if not TESTING:
    CELERY_BROKER_URL = os.getenv('REDIS_URL', 'redis://localhost/1')
else:
    CELERY_TASK_ALWAYS_EAGER = True
    CELERY_TASK_EAGER_PROPAGATES = True
    CELERY_BROKER_URL = 'memory://'

LOGGING = {
    'version': 1,
    'filters': {'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'}},
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
}

if not TESTING and SHELL:
    LOGGING.update(
        {
            'loggers': {
                'django.db.backends': {
                    'level': 'DEBUG',
                    'handlers': ['console'],
                    'propagate': False,
                },
            }
        }
    )

DJANGO_LOCI_GEOCODE_STRICT_TEST = False
OPENWISP_CONTROLLER_CONTEXT = {'vpnserver1': 'vpn.testdomain.com'}
OPENWISP_USERS_AUTH_API = True

TEST_RUNNER = 'immunity_utils.tests.TimeLoggingTestRunner'

if os.environ.get('SAMPLE_APP', False):
    # Replace Config
    config_index = INSTALLED_APPS.index('immunity_controller.config')
    INSTALLED_APPS.remove('immunity_controller.config')
    INSTALLED_APPS.insert(config_index, 'immunity22.sample_config')
    # Replace Pki
    pki_index = INSTALLED_APPS.index('immunity_controller.pki')
    INSTALLED_APPS.remove('immunity_controller.pki')
    INSTALLED_APPS.insert(pki_index, 'immunity22.sample_pki')
    # Replace Geo
    geo_index = INSTALLED_APPS.index('immunity_controller.geo')
    INSTALLED_APPS.remove('immunity_controller.geo')
    INSTALLED_APPS.insert(geo_index, 'immunity22.sample_geo')
    # Replace Connection
    connection_index = INSTALLED_APPS.index('immunity_controller.connection')
    INSTALLED_APPS.remove('immunity_controller.connection')
    INSTALLED_APPS.insert(connection_index, 'immunity22.sample_connection')
    # Replace Openwisp_Users
    users_index = INSTALLED_APPS.index('immunity_users')
    INSTALLED_APPS.remove('immunity_users')
    INSTALLED_APPS.insert(users_index, 'immunity22.sample_users')
    # Replace Subnet Division
    subnet_division_index = INSTALLED_APPS.index('immunity_controller.subnet_division')
    INSTALLED_APPS.remove('immunity_controller.subnet_division')
    INSTALLED_APPS.insert(subnet_division_index, 'immunity22.sample_subnet_division')
    # Extended apps
    EXTENDED_APPS = (
        'django_x509',
        'django_loci',
        'immunity_controller.config',
        'immunity_controller.pki',
        'immunity_controller.geo',
        'immunity_controller.connection',
        'immunity_controller.subnet_division',
        'immunity_users',
    )
    # Swapper
    AUTH_USER_MODEL = 'sample_users.User'
    OPENWISP_USERS_GROUP_MODEL = 'sample_users.Group'
    OPENWISP_USERS_ORGANIZATION_MODEL = 'sample_users.Organization'
    OPENWISP_USERS_ORGANIZATIONUSER_MODEL = 'sample_users.OrganizationUser'
    OPENWISP_USERS_ORGANIZATIONOWNER_MODEL = 'sample_users.OrganizationOwner'
    OPENWISP_USERS_ORGANIZATIONINVITATION_MODEL = 'sample_users.OrganizationInvitation'
    CONFIG_DEVICE_MODEL = 'sample_config.Device'
    CONFIG_DEVICEGROUP_MODEL = 'sample_config.DeviceGroup'
    CONFIG_CONFIG_MODEL = 'sample_config.Config'
    CONFIG_TEMPLATETAG_MODEL = 'sample_config.TemplateTag'
    CONFIG_TAGGEDTEMPLATE_MODEL = 'sample_config.TaggedTemplate'
    CONFIG_TEMPLATE_MODEL = 'sample_config.Template'
    CONFIG_VPN_MODEL = 'sample_config.Vpn'
    CONFIG_VPNCLIENT_MODEL = 'sample_config.VpnClient'
    CONFIG_ORGANIZATIONCONFIGSETTINGS_MODEL = 'sample_config.OrganizationConfigSettings'
    CONFIG_ORGANIZATIONLIMITS_MODEL = 'sample_config.OrganizationLimits'
    DJANGO_X509_CA_MODEL = 'sample_pki.Ca'
    DJANGO_X509_CERT_MODEL = 'sample_pki.Cert'
    GEO_LOCATION_MODEL = 'sample_geo.Location'
    GEO_FLOORPLAN_MODEL = 'sample_geo.FloorPlan'
    GEO_DEVICELOCATION_MODEL = 'sample_geo.DeviceLocation'
    CONNECTION_CREDENTIALS_MODEL = 'sample_connection.Credentials'
    CONNECTION_DEVICECONNECTION_MODEL = 'sample_connection.DeviceConnection'
    CONNECTION_COMMAND_MODEL = 'sample_connection.Command'
    SUBNET_DIVISION_SUBNETDIVISIONRULE_MODEL = (
        'sample_subnet_division.SubnetDivisionRule'
    )
    SUBNET_DIVISION_SUBNETDIVISIONINDEX_MODEL = (
        'sample_subnet_division.SubnetDivisionIndex'
    )
else:
    # not needed, these are the default values, left here only for example purposes
    # DJANGO_X509_CA_MODEL = 'pki.Ca'
    # DJANGO_X509_CERT_MODEL = 'pki.Cert'
    pass

if os.environ.get('SAMPLE_APP', False) and TESTING:
    # Required for immunity-users tests
    OPENWISP_ORGANIZATION_USER_ADMIN = True
    OPENWISP_ORGANIZATION_OWNER_ADMIN = True
    OPENWISP_USERS_AUTH_API = True

# local settings must be imported before test runner otherwise they'll be ignored
try:
    from .local_settings import *
except ImportError:
    pass
