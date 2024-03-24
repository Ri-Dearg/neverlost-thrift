"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys

# Uses env.py for environment variales when local
try:
    import env  # noqa: F401
except ModuleNotFoundError:
    # Error handling
    pass


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
DEVELOPMENT = os.getenv("DEVELOPMENT")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", False)
if DEBUG == "True":
    print("Debug mode is on.")
elif DEBUG is False:
    print("Debug mode is off.")

ALLOWED_HOSTS = ["localhost"]

# Add Render.com URL to allowed hosts
RENDER_EXTERNAL_HOSTNAME = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Postgres specific functions
    "django.contrib.postgres",
    # Required for aullauth
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # Used for model and form fields
    "django_countries",
    "phonenumber_field",
    # App for connecting to AWS
    "storages",
    # App for automatic form styling
    "crispy_forms",
    # Apps for compiling SASS
    "sass_processor",
    "compressor",
    # For ajax decorator
    "django_ajax",
    # My apps
    "cart",
    "checkout",
    "contact",
    "likes",
    "products",
    "users",
]

SITE_ID = 1

# Settings for django-allauth
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_ADAPTER = "users.adapter.CustomAdapter"
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

# Settings for django-countries
COUNTRIES_FIRST = ["IE", "GB"]

# Settings for phonenumber-field
PHONENUMBER_DB_FORMAT = "E164"

# Crispy forms CSS template selection
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Settings for SASS compiling
SASS_PRECISION = 8
COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)
SASS_PROCESSOR_ROOT = "static/"
COMPRESS_ROOT = "static"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Deploys static files in production
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Uses templates in a base directory for all apps
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                # `allauth` needs this from django
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Custom context Processors for allauth forms
                "users.context_processors.login_form",
                "users.context_processors.signup_form",
                # Processor for the cart
                "cart.context_processors.get_cart",
                "likes.context_processors.get_likes",
                "products.context_processors.get_stockdrops",
                "products.context_processors.get_categories",
            ],
        },
    },
]

# Necessary to show messages in GitPod
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]


WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PGDATABASE"),
        "USER": os.getenv("PGUSER"),
        "PASSWORD": os.getenv("PGPASSWORD"),
        "HOST": os.getenv("PGHOST"),
        "PORT": os.getenv("PGPORT", "5432"),
        "OPTIONS": {
            "sslmode": "require",
        },
        "DISABLE_SERVER_SIDE_CURSORS": True,
        "TEST": {
            "NAME": "testdb",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501
    },
]


# Finders for different types off files
STATICFILES_FINDERS = [
    # Default finders
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # finders for sass files
    "sass_processor.finders.CssFinder",
    "compressor.finders.CompressorFinder",
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Rome"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Static files are maintained in a base directory
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# supabase storage settings
DEFAULT_FILE_STORAGE = "custom_storages.SupabaseStorage"
SUPABASE_KEY = os.getenv("SUPABASE_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
BUCKET_NAME = os.getenv("BUCKET_NAME")
SUPABASE_ROOT_PATH = "/dir/"

# Checks for the Development variable. If not found it uses AWS.
if not DEVELOPMENT:
    # Settings for AWS bucket
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31, Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }

    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = "eu-west-3"
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

    STATICFILES_LOCATION = "static"
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"

    # Media Settings
    MEDIAFILES_LOCATION = "media"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"

# Sets the cost limit for free delivery.
FREE_DELIVERY_THRESHOLD = 60
STANDARD_DELIVERY = 9

# Necessary variables and setting to take Stripe Payments.
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET", "")
STRIPE_CURRENCY = "eur"

# If in development, emails are displayed in the terminal
if "DEVELOPMENT" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = "example@example.com"

# Else emails are sent using real account settings
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASS")
    DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER")

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
