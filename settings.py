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

PASSWORD_PROTECT_SITE = False

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
USE_I18N = False

# Absolute path to the directory that holds user generated media.
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")
# Relative to user generated media
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
ADMIN_MEDIA_PREFIX = '/media/admin/'
MODEL_IMAGES_ROOT = os.path.join(MEDIA_ROOT, 'images', 'models')

# Have to set this to false for some reason otherwise *all* urls come through with
# an appended slash for some reason, even if they do have a url match. Something
# to do with django-cms and the way it is handling url matching/routing
APPEND_SLASH = False

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

    'zinnia.context_processors.version', # Optional
    'zinnia.context_processors.media',
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
    'mailchimp',
    'sorl.thumbnail',
    'popularity',
    'south',
    'taggit',
    'filebrowser',
    'tinymce',
    'tagging',
    'zinnia', 
    'zinnia.plugins',
#    'genericforeignkey',
    
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
    "efocms",
    "images",
    "search",
    "features",
    "projects",
    "programmes",
    "efozinnia",
    "home",
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

# Zinnia blog engine
ZINNIA_HIDE_ENTRY_MENU = False

# Sorl Thumbnail
THUMBNAIL_BASEDIR = "cache"
THUMBNAIL_DEBUG = True

# Local Settings
try:
    from local_settings import *
except ImportError:
    pass

CMS_TEMPLATES = (
        (' base/general.html', gettext('general')),        
        ('base/base.html', gettext('base')),
        ('site_base.html', gettext('main base')),
        ('programmes/programmes_container.html', gettext('programmes container')),
        ('base/home.html', gettext('home')),
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

TINYMCE_JS_URL = MEDIA_URL + 'admin/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = MEDIA_ROOT + 'admin/tiny_mce'
TINYMCE_DEFAULT_CONFIG = {
                            'plugins': "table,paste,searchreplace",
                            'theme': "advanced",
                         }
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = False
TINYMCE_FILEBROWSER = True

FEATURED_COUNTRIES = (
    ('AU', (u'Australia')),
    ('NZ', (u'New Zealand')),
    ('',   (u'-------')),
    ('AF', (u'Afghanistan')),
    ('AX', (u'\xc5land Islands')),
    ('AL', (u'Albania')),
    ('DZ', (u'Algeria')),
    ('AS', (u'American Samoa')),
    ('AD', (u'Andorra')),
    ('AO', (u'Angola')),
    ('AI', (u'Anguilla')),
    ('AQ', (u'Antarctica')),
    ('AG', (u'Antigua and Barbuda')),
    ('AR', (u'Argentina')),
    ('AM', (u'Armenia')),
    ('AW', (u'Aruba')),
    # ('AU', (u'Australia')),
    ('AT', (u'Austria')),
    ('AZ', (u'Azerbaijan')),
    ('BS', (u'Bahamas')),
    ('BH', (u'Bahrain')),
    ('BD', (u'Bangladesh')),
    ('BB', (u'Barbados')),
    ('BY', (u'Belarus')),
    ('BE', (u'Belgium')),
    ('BZ', (u'Belize')),
    ('BJ', (u'Benin')),
    ('BM', (u'Bermuda')),
    ('BT', (u'Bhutan')),
    ('BO', (u'Bolivia, Plurinational State of')),
    ('BA', (u'Bosnia and Herzegovina')),
    ('BW', (u'Botswana')),
    ('BV', (u'Bouvet Island')),
    ('BR', (u'Brazil')),
    ('IO', (u'British Indian Ocean Territory')),
    ('BN', (u'Brunei Darussalam')),
    ('BG', (u'Bulgaria')),
    ('BF', (u'Burkina Faso')),
    ('BI', (u'Burundi')),
    ('KH', (u'Cambodia')),
    ('CM', (u'Cameroon')),
    ('CA', (u'Canada')),
    ('CV', (u'Cape Verde')),
    ('KY', (u'Cayman Islands')),
    ('CF', (u'Central African Republic')),
    ('TD', (u'Chad')),
    ('CL', (u'Chile')),
    ('CN', (u'China')),
    ('CX', (u'Christmas Island')),
    ('CC', (u'Cocos (Keeling) Islands')),
    ('CO', (u'Colombia')),
    ('KM', (u'Comoros')),
    ('CG', (u'Congo')),
    ('CD', (u'Congo, The Democratic Republic of the')),
    ('CK', (u'Cook Islands')),
    ('CR', (u'Costa Rica')),
    ('CI', (u"C\xf4te D'ivoire")),
    ('HR', (u'Croatia')),
    ('CU', (u'Cuba')),
    ('CY', (u'Cyprus')),
    ('CZ', (u'Czech Republic')),
    ('DK', (u'Denmark')),
    ('DJ', (u'Djibouti')),
    ('DM', (u'Dominica')),
    ('DO', (u'Dominican Republic')),
    ('EC', (u'Ecuador')),
    ('EG', (u'Egypt')),
    ('SV', (u'El Salvador')),
    ('GQ', (u'Equatorial Guinea')),
    ('ER', (u'Eritrea')),
    ('EE', (u'Estonia')),
    ('ET', (u'Ethiopia')),
    ('FK', (u'Falkland Islands (Malvinas)')),
    ('FO', (u'Faroe Islands')),
    ('FJ', (u'Fiji')),
    ('FI', (u'Finland')),
    ('FR', (u'France')),
    ('GF', (u'French Guiana')),
    ('PF', (u'French Polynesia')),
    ('TF', (u'French Southern Territories')),
    ('GA', (u'Gabon')),
    ('GM', (u'Gambia')),
    ('GE', (u'Georgia')),
    ('DE', (u'Germany')),
    ('GH', (u'Ghana')),
    ('GI', (u'Gibraltar')),
    ('GR', (u'Greece')),
    ('GL', (u'Greenland')),
    ('GD', (u'Grenada')),
    ('GP', (u'Guadeloupe')),
    ('GU', (u'Guam')),
    ('GT', (u'Guatemala')),
    ('GG', (u'Guernsey')),
    ('GN', (u'Guinea')),
    ('GW', (u'Guinea-bissau')),
    ('GY', (u'Guyana')),
    ('HT', (u'Haiti')),
    ('HM', (u'Heard Island and McDonald Islands')),
    ('VA', (u'Holy See (Vatican City State)')),
    ('HN', (u'Honduras')),
    ('HK', (u'Hong Kong')),
    ('HU', (u'Hungary')),
    ('IS', (u'Iceland')),
    ('IN', (u'India')),
    ('ID', (u'Indonesia')),
    ('IR', (u'Iran, Islamic Republic of')),
    ('IQ', (u'Iraq')),
    ('IE', (u'Ireland')),
    ('IM', (u'Isle of Man')),
    ('IL', (u'Israel')),
    ('IT', (u'Italy')),
    ('JM', (u'Jamaica')),
    ('JP', (u'Japan')),
    ('JE', (u'Jersey')),
    ('JO', (u'Jordan')),
    ('KZ', (u'Kazakhstan')),
    ('KE', (u'Kenya')),
    ('KI', (u'Kiribati')),
    ('KP', (u"Korea, Democratic People's Republic of")),
    ('KR', (u'Korea, Republic of')),
    ('KW', (u'Kuwait')),
    ('KG', (u'Kyrgyzstan')),
    ('LA', (u"Lao People's Democratic Republic")),
    ('LV', (u'Latvia')),
    ('LB', (u'Lebanon')),
    ('LS', (u'Lesotho')),
    ('LR', (u'Liberia')),
    ('LY', (u'Libyan Arab Jamahiriya')),
    ('LI', (u'Liechtenstein')),
    ('LT', (u'Lithuania')),
    ('LU', (u'Luxembourg')),
    ('MO', (u'Macao')),
    ('MK', (u'Macedonia, The Former Yugoslav Republic of')),
    ('MG', (u'Madagascar')),
    ('MW', (u'Malawi')),
    ('MY', (u'Malaysia')),
    ('MV', (u'Maldives')),
    ('ML', (u'Mali')),
    ('MT', (u'Malta')),
    ('MH', (u'Marshall Islands')),
    ('MQ', (u'Martinique')),
    ('MR', (u'Mauritania')),
    ('MU', (u'Mauritius')),
    ('YT', (u'Mayotte')),
    ('MX', (u'Mexico')),
    ('FM', (u'Micronesia, Federated States of')),
    ('MD', (u'Moldova, Republic of')),
    ('MC', (u'Monaco')),
    ('MN', (u'Mongolia')),
    ('ME', (u'Montenegro')),
    ('MS', (u'Montserrat')),
    ('MA', (u'Morocco')),
    ('MZ', (u'Mozambique')),
    ('MM', (u'Myanmar')),
    ('NA', (u'Namibia')),
    ('NR', (u'Nauru')),
    ('NP', (u'Nepal')),
    ('NL', (u'Netherlands')),
    ('AN', (u'Netherlands Antilles')),
    ('NC', (u'New Caledonia')),
    # ('NZ', (u'New Zealand')),
    ('NI', (u'Nicaragua')),
    ('NE', (u'Niger')),
    ('NG', (u'Nigeria')),
    ('NU', (u'Niue')),
    ('NF', (u'Norfolk Island')),
    ('MP', (u'Northern Mariana Islands')),
    ('NO', (u'Norway')),
    ('OM', (u'Oman')),
    ('PK', (u'Pakistan')),
    ('PW', (u'Palau')),
    ('PS', (u'Palestinian Territory, Occupied')),
    ('PA', (u'Panama')),
    ('PG', (u'Papua New Guinea')),
    ('PY', (u'Paraguay')),
    ('PE', (u'Peru')),
    ('PH', (u'Philippines')),
    ('PN', (u'Pitcairn')),
    ('PL', (u'Poland')),
    ('PT', (u'Portugal')),
    ('PR', (u'Puerto Rico')),
    ('QA', (u'Qatar')),
    ('RE', (u'R\xe9union')),
    ('RO', (u'Romania')),
    ('RU', (u'Russian Federation')),
    ('RW', (u'Rwanda')),
    ('BL', (u'Saint Barth\xe9lemy')),
    ('SH', (u'Saint Helena, Ascension and Tristan Da Cunha')),
    ('KN', (u'Saint Kitts and Nevis')),
    ('LC', (u'Saint Lucia')),
    ('MF', (u'Saint Martin')),
    ('PM', (u'Saint Pierre and Miquelon')),
    ('VC', (u'Saint Vincent and the Grenadines')),
    ('WS', (u'Samoa')),
    ('SM', (u'San Marino')),
    ('ST', (u'Sao Tome and Principe')),
    ('SA', (u'Saudi Arabia')),
    ('SN', (u'Senegal')),
    ('RS', (u'Serbia')),
    ('SC', (u'Seychelles')),
    ('SL', (u'Sierra Leone')),
    ('SG', (u'Singapore')),
    ('SK', (u'Slovakia')),
    ('SI', (u'Slovenia')),
    ('SB', (u'Solomon Islands')),
    ('SO', (u'Somalia')),
    ('ZA', (u'South Africa')),
    ('GS', (u'South Georgia and the South Sandwich Islands')),
    ('ES', (u'Spain')),
    ('LK', (u'Sri Lanka')),
    ('SD', (u'Sudan')),
    ('SR', (u'Suriname')),
    ('SJ', (u'Svalbard and Jan Mayen')),
    ('SZ', (u'Swaziland')),
    ('SE', (u'Sweden')),
    ('CH', (u'Switzerland')),
    ('SY', (u'Syrian Arab Republic')),
    ('TW', (u'Taiwan, Province of China')),
    ('TJ', (u'Tajikistan')),
    ('TZ', (u'Tanzania, United Republic of')),
    ('TH', (u'Thailand')),
    ('TL', (u'Timor-leste')),
    ('TG', (u'Togo')),
    ('TK', (u'Tokelau')),
    ('TO', (u'Tonga')),
    ('TT', (u'Trinidad and Tobago')),
    ('TN', (u'Tunisia')),
    ('TR', (u'Turkey')),
    ('TM', (u'Turkmenistan')),
    ('TC', (u'Turks and Caicos Islands')),
    ('TV', (u'Tuvalu')),
    ('UG', (u'Uganda')),
    ('UA', (u'Ukraine')),
    ('AE', (u'United Arab Emirates')),
    ('GB', (u'United Kingdom')),
    ('US', (u'United States')),
    ('UM', (u'United States Minor Outlying Islands')),
    ('UY', (u'Uruguay')),
    ('UZ', (u'Uzbekistan')),
    ('VU', (u'Vanuatu')),
    ('VE', (u'Venezuela, Bolivarian Republic of')),
    ('VN', (u'Viet Nam')),
    ('VG', (u'Virgin Islands, British')),
    ('VI', (u'Virgin Islands, U.S.')),
    ('WF', (u'Wallis and Futuna')),
    ('EH', (u'Western Sahara')),
    ('YE', (u'Yemen')),
    ('ZM', (u'Zambia')),
    ('ZW', (u'Zimbabwe')),

)    
