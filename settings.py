import os
import posixpath
import pinax
import sys

#a local change

gettext = lambda s: s

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
PROJECT_FOLDER = os.path.dirname(__file__).split('/')[-1]
sys.path.insert(0, os.path.join(PROJECT_ROOT))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

# tells Pinax to use the default theme
PINAX_THEME = "pinax-designer-theme"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    # ("Your Name", "your_email@domain.com"),
]

CONTACT_EMAIL = 'info@empty-django-cms-project.com'

MANAGERS = ADMINS

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/welcome'
LOGIN_URL = '/login'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Melbourne'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1
SITE_NAME = "Empty Django Cms Project"

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/site_media/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "media"),
    os.path.join(PROJECT_ROOT, "media", PINAX_THEME), # ship 'with' the project for now.
    # revert to the Pinax default whilst design_five is in development
    os.path.join(PINAX_ROOT, "media", "default"),
    
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")
ADMIN_MEDIA_ROOT = os.path.join(STATIC_ROOT, 'admin')
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
MODEL_IMAGES_ROOT = os.path.join(MEDIA_ROOT, 'images', 'models')

# Make this unique, and don't share it with anybody.
SECRET_KEY = "unzj&n1$^ox6%-xh490357i=l@wmq!lu&toe=*sj8s2qv73mhr"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "django_openid.consumer.SessionConsumer",
    "django.contrib.messages.middleware.MessageMiddleware",
    "pinax.apps.account.middleware.LocaleMiddleware",
    "pagination.middleware.PaginationMiddleware",
    "pinax.middleware.security.HideSensistiveFieldsMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware', #2.1 beta 3 only
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
]

ROOT_URLCONF = PROJECT_FOLDER + ".urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PROJECT_ROOT, "templates", PINAX_THEME), # ship 'with' the project for now.
    # revert to the Pinax default whilst design_five is in development
    os.path.join(PINAX_ROOT, "templates", "default")
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    
    "staticfiles.context_processors.static_url",
    "pinax.core.context_processors.pinax_settings",
    "pinax.apps.account.context_processors.account",
    "notification.context_processors.notification",
    "announcements.context_processors.site_wide_announcements",
    'popularity.context_processors.most_popular',
    'popularity.context_processors.most_viewed',
    'popularity.context_processors.recently_viewed',
    'popularity.context_processors.recently_added',
    'cms.context_processors.media',
]

INSTALLED_APPS = [
    # external
    "notification", # must be first
    
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.databrowse",
    "django.contrib.comments",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    
    # Assorted 3rd party
    "staticfiles",
    "debug_toolbar",
    "django_extensions",
    "mailer",
    "uni_form",
    "django_openid",
    "ajax_validation",
    "timezones",
    "emailconfirmation",
    "announcements",
    "pagination",
    "idios",
    "endless_pagination",
    'filebrowser',
    'mailchimp',
    'sorl.thumbnail',
    'popularity',
    'south',
    'taggit',
    
    # Pinax
    "pinax.templatetags",
    "pinax.apps.analytics",

    #django-cms
    'cms',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.text',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'mptt',
    'menus', #2.1 beta 3 only
    
    #project apps
    "pinax_local.apps.account",
    "profiles",
]

# Database

DATABASE_ROUTERS = [
]

# Fixtures
FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

# Messages
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/%s/" % o.username,
}

# Accounts / Profiles
AUTH_PROFILE_MODULE = "profiles.Profile"

NOTIFICATION_LANGUAGE_MODULE = "account.Account"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_EMAIL_AUTHENTICATION = True
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

AUTHENTICATION_BACKENDS = [
    "profiles.auth_backends.AuthenticationBackend",
]

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?
LOGIN_REDIRECT_URLNAME = "home"

# Debugging Toolbar
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

# Filebrowser
FILEBROWSER_DEBUG = False
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_URL_FILEBROWSER_MEDIA = STATIC_URL + 'filebrowser/'
FILEBROWSER_PATH_FILEBROWSER_MEDIA = STATIC_ROOT + 'filebrowser/'
FILEBROWSER_DIRECTORY = 'files/'

FILEBROWSER_SAVE_FULL_URL = False
FILEBROWSER_VERSIONS_BASEDIR = "cache"

# Google Analytics
# URCHIN_ID = "ua-..."

# Mailchimp
MAILCHIMP_API_KEY = '1' # dummy
MAILCHIMP_WEBHOOK_KEY = '1'
MAILCHIMP_LIST_ID = '1' # dummy 

# Sorl Thumbnail
THUMBNAIL_BASEDIR = "cache"
THUMBNAIL_DEBUG = False

# Local Settings
try:
    from local_settings import *
except ImportError:
    pass

# @@@ To be moved to entropy

CMS_TEMPLATES = (
        ('general.html', gettext('general')),        
        ('base.html', gettext('base')),
        ('home.html', gettext('home')),
)

LANGUAGES = (
    ('en', gettext('English')),
)

CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_FLAT_URLS = False
CMS_MENU_TITLE_OVERWRITE = True
CMS_HIDE_UNTRANSLATED = False
CMS_URL_OVERWRITE = True

CMS_MODERATOR = False
CMS_SHOW_END_DATE = True
CMS_SHOW_START_DATE = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_UNIQUE_SLUGS = True
CMS_CONTENT_CACHE_DURATION = 10

TINYMCE_JS_URL = MEDIA_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = MEDIA_ROOT + 'js/tiny_mce'
TINYMCE_DEFAULT_CONFIG = {
                            'plugins': "table,paste,searchreplace",
                            'theme': "advanced",
                         }
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = False
