import os
from pathlib import Path
from django.contrib.messages import constants as messages
import dj_database_url
from django.core.mail import send_mail
from django.conf import settings


if os.path.isfile("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/c/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# .ENV local settings.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get("DEBUG")) == "1"  # 1 == True
RUN_UNITTESTS = str(os.environ.get("RUN_UNITTESTS")) == "1"  # 1 == True
RUN_LOCALONLY = str(os.environ.get("RUN_LOCALONLY")) == "1"  # 1 == True

if DEBUG:
    ALLOWED_HOSTS = [os.environ.get("ENV_ALLOWED_HOSTS")]
    if RUN_UNITTESTS:
        RUN_UNITTESTS = str(os.environ.get("RUN_UNITTESTS")) == "1"  # 1 == True
else:
    X_FRAME_OPTIONS = "SAMEORIGIN"
    if RUN_LOCALONLY:
        ALLOWED_HOSTS = [os.environ.get("ENV_ALLOWED_HOSTS")]
    else:
        ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]

# Add Render.com URL to allowed hosts
 RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
 if RENDER_EXTERNAL_HOSTNAME:
   ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "import_export",
    "cloudinary_storage",
    "cloudinary",
    "django_summernote",
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "leannes_learners_data",
    "blog",
    "users",
]

SITE_ID = 1

LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "leannes_learners.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "blog.views.category_list",
                "leannes_learners_data.views.social_icons_list",
            ],
        },
    },
]

WSGI_APPLICATION = "leannes_learners.wsgi.application"


# Database
if RUN_UNITTESTS is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "db.sqlite3",
        }
    }
else:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "/leannes_learners/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# test email server setup
if RUN_UNITTESTS is True:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    EMAIL_HOST = "127.0.0.1"
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ""
    EMAIL_HOST_PASSWORD = ""
    EMAIL_USE_TLS = False
    RECIPIENT_ADDRESS = "testing@example.com"
    DEFAULT_FROM_EMAIL = "testing@example.com"
else:
    # TODO Deployment update email settings
    # Email Settings
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "mail.leanneslearners.com"
    EMAIL_HOST_USER = "noreply@leanneslearners.com"
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = "587"
    RECIPIENT_ADDRESS = "test-noreply@leanneslearners.com"  # default To email
    DEFAULT_FROM_EMAIL = "Leannes Learners <test-noreply@leanneslearners.com>"

SUMMERNOTE_CONFIG = {
    "iframe": True,
    "summernote": {
        "width": "100%",
        "height": "600px",
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "underline", "clear"]],
            ["fontname", ["fontname"]],
            ["color", ["color"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["table", ["table"]],
            ["insert", ["link", "picture", "video"]],
            ["view", ["fullscreen", "codeview", "help"]],
            ["custom", ["imageAttributes", "imageShape"]],
        ],
    },
    "popover": {
        "image": [
            ["custom", ["imageAttributes"]],
            ["imagesize", ["imageSize100", "imageSize50", "imageSize25"]],
            ["float", ["floatLeft", "floatRight", "floatNone"]],
            ["remove", ["removeMedia"]],
        ],
    },
    "js": ("/static/js/summernote-image-attributes.js",),
    "js_for_inplace": ("/static/js/summernote-image-attributes.js",),
}
