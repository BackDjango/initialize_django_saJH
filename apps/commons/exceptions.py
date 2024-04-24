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


class AlreadyExistException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Already exist."
    default_code = "already_exist"


class InvalidTokenException(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Invalid token."
    default_code = "invalid_token"


class AuthenticationFailedException(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Incorrect authentication credentials."
    default_code = "authentication_failed"
