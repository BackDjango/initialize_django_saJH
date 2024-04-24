from typing import Any, Dict, Optional

from rest_framework import status
from rest_framework.response import Response


def create_response(
    data: Optional[dict] = None,
    code: Optional[str] = "request_success",
    message: Optional[str] = "Request was successful.",
    status_code: int = status.HTTP_200_OK,
    **kwargs: Any,
) -> Response:
    json_data: Dict[str, Any] = {}
    json_data["success"] = True if status.is_success(status_code) else False
    json_data["code"] = code
    json_data["message"] = message
    json_data["data"] = data or {}
    return Response(json_data, status=status_code, **kwargs)
