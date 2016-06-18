from site_settings import *
import os

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ')71$p073b5%a7l@23g%jybphk=qpf&okk%4^+1k457u_$b#3s_'

ROOT_URLCONF = 'mon_site.urls'

WSGI_APPLICATION = 'mon_site.wsgi.application'

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR,"..",'media')
STATIC_ROOT = os.path.join(DATA_DIR,"..", 'static')

STATICFILES_DIRS = (
    #  os.path.join(DATA_DIR, 'mon_site', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mon_site', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'filer',
    'easy_thumbnails',
    'image_gallery',
    'captcha',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_utils',
    'cmsplugin_contact_plus',
    # 'djangocms_column',
    # 'cmsplugin_filer_folder',
    # 'cmsplugin_filer_teaser',
    # 'cmsplugin_filer_video',
    # 'djangocms_inherit',
    # 'djangocms_link',
    'reversion',
    'django_extensions',
    'leaflet',
    'tour_mgmt',
    'mon_site'
)

LANGUAGES = (
    ## Customize this
    ('fr', gettext('fr')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback': True,
            'code': 'fr',
            'name': gettext('fr'),
        },
    ],
    'default': {
        'hide_untranslated': False,
        'redirect_on_fallback': True,
        'public': True,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('homepage.html', 'Gabarit Homepage'),
    ('tierstruck_lozere.html', 'Gabarit TiersTruck_lozere'),
    ('tierstrucker.html', 'Gabarit TiersTrucker'),
    ('3_col.html', '3 colonnes'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

MIGRATION_MODULES = {
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django'
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

LEAFLET_CONFIG = {
    # 'DEFAULT_CENTER': (44.5257868, 3.4860797),
    'DEFAULT_CENTER': (44.526, 3.6),
    'DEFAULT_ZOOM': 8,
    'MIN_ZOOM': 1,
    'MAX_ZOOM': 17,
    'TILES': 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
}
