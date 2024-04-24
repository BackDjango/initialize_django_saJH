from rest_framework import status

from apps.commons.base.exceptions import BaseAPIException


class UnknownServerException(BaseAPIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "An unknown server error occurred."
    default_code = "unknown_server_error"


class InvalidParameterFormatException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "The parameter format is incorrect."
    default_code = "invalid_parameter_format"


class ValidationException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Validation failed."
    default_code = "validation_failed"
