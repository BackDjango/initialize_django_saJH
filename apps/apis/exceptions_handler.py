from datetime import datetime

from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from apps.apis.response import create_response
from apps.commons.exceptions import UnknownServerException, ValidationException
from config.settings.logging import logger


def default_exception_handler(exc: Exception, context: dict) -> Response:
    logger.error("[EXCEPTION_HANDLER]")
    logger.error(f"[{datetime.now()}]")
    logger.error("> exc")
    logger.error(f"{exc}")
    logger.error("> context")
    logger.error(f"{context}")

    if isinstance(exc, APIException):
        response = handle_api_exception(exc=exc, context=context)

    if isinstance(exc, ValidationError):
        response = handle_django_validation_exception(exc=exc, context=context)

    if "response" in locals():
        return response

    return handle_api_exception(exc=UnknownServerException(), context=context)


def handle_api_exception(exc: APIException, context: dict) -> Response:
    message = getattr(exc, "detail")
    status_code = getattr(exc, "status_code")

    if hasattr(message, "code"):
        code = getattr(message, "code")
    else:
        code = getattr(exc, "default_code")

    return create_response(code=code, message=message, status_code=status_code)


def handle_django_validation_exception(exc: ValidationError, context: dict) -> Response:
    status_code = getattr(ValidationException, "status_code")
    code = getattr(ValidationException, "default_code")

    if hasattr(exc, "message_dict"):
        message = getattr(exc, "message_dict")
    else:
        message = exc

    return create_response(code=code, message=message, status_code=status_code)
