"""
Django settings for seolondon project.

Generated by 'django-admin startproject' using Django 1.8.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

#PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

gettext = lambda s: s

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
ALLOWED_HOSTS = []

DEBUG = True

SECRET_KEY = 'FAKEforDEV'
# Application definition


ROOT_URLCONF = 'seolondon.urls'

WSGI_APPLICATION = 'seolondon.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/London'

USE_I18N = False

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
#STATICFILES_DIRS = (
#

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'seolondon', 'templates'), ],
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
                'cms.context_processors.cms_settings',
                'seolondon.context_processors.google_tracking'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = [
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
]

INSTALLED_APPS = [
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
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'reversion',
    'seolondon',
    'djangocms_repeater',
    'djangocms_plain_text',
    'storages',
]

LANGUAGES = (
    ('en', gettext('en')),
)

CMS_MAX_PAGE_PUBLISH_REVERSIONS = 5

CMS_LANGUAGES = {
    1: [
        {
            'hide_untranslated': False,
            'code': 'en',
            'redirect_on_fallback': True,
            'public': True,
            'name': gettext('en'),
        },
    ],
    'default': {
        'public': True,
        'redirect_on_fallback': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ('homepage.html', 'Homepage'),
    ('careers.html', 'Careers Landing Page'),
    ('careers-inner.html', 'Careers Inner Page'),
    ('careers-inner-corporates.html', 'Careers Inner (Corporates) Page'),
    ('careers-inner-civil.html', 'Careers Inner (Civil Service) Page'),
    ('scholars.html', 'Scholars Page'),
    ('about.html', 'About Page'),
    ('get-involved.html', 'Get Involved Page'),
    ('success-stories.html', 'Success Stories Page'),
    ('who-we-support.html', 'Who We Support Page'),
    ('connect.html', 'Connect Page'),
    ('plain.html', 'Plain Page'),
    ('faq.html', 'FAQ Page'),
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'seolondon',
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'seolondon',
            'USER': 'seolondon',
            'PASSWORD': 'seolondon',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

MIGRATION_MODULES = {

}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# User image uploads to S3 bucket
# AWS keys
AWS_SECRET_ACCESS_KEY = os.environ.get("SEO_AWS_SECRET_ACCESS_KEY", '')
AWS_ACCESS_KEY_ID = os.environ.get("SEO_AWS_ACCESS_KEY_ID", '')
AWS_STORAGE_BUCKET_NAME = os.environ.get("SEO_AWS_STORAGE_BUCKET_NAME", "seo-london-images")
AWS_PRIVATE_STORAGE_BUCKET_NAME = os.environ.get(
        "SEO_AWS_STORAGE_BUCKET_NAME", AWS_STORAGE_BUCKET_NAME)
AWS_S3_REGION_NAME = os.environ.get('SEO_AWS_S3_REGION_NAME', None)

FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'storages.backends.s3boto3.S3Boto3Storage',
            'OPTIONS': {
                'access_key': AWS_ACCESS_KEY_ID,
                'secret_key': AWS_SECRET_ACCESS_KEY,
                'bucket_name': AWS_STORAGE_BUCKET_NAME,
                'region_name': AWS_S3_REGION_NAME,
                'addressing_style': 'auto',
                'signature_version': 's3v4'
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'storages.backends.s3boto3.S3Boto3Storage',
            'OPTIONS': {
                'access_key': AWS_ACCESS_KEY_ID,
                'secret_key': AWS_SECRET_ACCESS_KEY,
                'bucket_name': AWS_STORAGE_BUCKET_NAME,
                'region_name': AWS_S3_REGION_NAME,
                'addressing_style': 'auto',
                'signature_version': 's3v4'
            },
        },
    },
    'private': {
        'main': {
            'ENGINE': 'storages.backends.s3boto3.S3Boto3Storage',
            'OPTIONS': {
                'access_key': AWS_ACCESS_KEY_ID,
                'secret_key': AWS_SECRET_ACCESS_KEY,
                'bucket_name': AWS_PRIVATE_STORAGE_BUCKET_NAME,
                'region_name': AWS_S3_REGION_NAME,
                'addressing_style': 'auto',
                'signature_version': 's3v4'
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_private',
        },
        'thumbnails': {
            'ENGINE': 'storages.backends.s3boto3.S3Boto3Storage',
            'OPTIONS': {
                'access_key': AWS_ACCESS_KEY_ID,
                'secret_key': AWS_SECRET_ACCESS_KEY,
                'bucket_name': AWS_PRIVATE_STORAGE_BUCKET_NAME,
                'region_name': AWS_S3_REGION_NAME,
                'addressing_style': 'auto',
                'signature_version': 's3v4'

            },
        },
    },
}

GOOGLE_ANALYTICS_TRACKING_ID = os.environ.get('GOOGLE_ANALYTICS_TRACKING_ID', '')
GOOGLE_GTM_CONTAINER_ID = os.environ.get('GOOGLE_GTM_CONTAINER_ID', '')
