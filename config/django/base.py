import os

from config.env import BASE_DIR, APPS_DIR, env

SERVER_ENV = os.environ.get("DJANGO_SETTINGS_MODULE", "config.django.base")

env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = "test"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# ==================================================================== #
#                     설치된 앱, 사용하는 앱 config                         #
# ==================================================================== #
LOCAL_APPS = [
    "apps.commons.apps.CommonsConfig",
    "apps.users.apps.UsersConfig",
    "apps.apis.apps.ApisConfig",
    "apps.boards.apps.BoardsConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.root_urls"

APPEND_SLASH = False

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(APPS_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"


# Password validation
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


AUTH_USER_MODEL = "users.User"

APP_DOMAIN = env("APP_DOMAIN", default="http://localhost:8000")

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Internationalization
LANGUAGE_CODE = "en-us"  # 언어 - 국가 설정

TIME_ZONE = "Asia/Seoul"  # 시간대 설정

USE_I18N = True  # 국제화

USE_L10N = True  # 지역화

USE_TZ = False  # 장고 시간대 사용 여부


# ==================================================================== #
#                  file system (static) config                         #
# ==================================================================== #
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# ==================================================================== #
#                       DRF config                                     #
# ==================================================================== #
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("djangorestframework_camel_case.render.CamelCaseJSONRenderer",),
    "DEFAULT_PARSER_CLASSES": ("djangorestframework_camel_case.parser.CamelCaseJSONParser",),
    "EXCEPTION_HANDLER": "apps.apis.exceptions_handler.default_exception_handler",
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
}


from config.settings.jwt import *  # noqa
from config.settings.logging import *  # noqa

from config.settings.swagger.settings import *  # noqa
from config.settings.swagger.setup import SwaggerSetup  # noqa

INSTALLED_APPS = SwaggerSetup.do_settings(INSTALLED_APPS)
