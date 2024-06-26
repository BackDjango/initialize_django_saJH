from rest_framework import status
from rest_framework.exceptions import APIException


class BaseAPIException(APIException):
    status_code: int = status.HTTP_400_BAD_REQUEST
    default_detail: str = "Bad request."
    default_code: str = "bad_request"
