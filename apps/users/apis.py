from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class SignUpAPI(APIView):
    @swagger_auto_schema(
        tags=["유저"],
        operation_summary="회원가입",
        operation_description="회원가입을 합니다.",
    )
    def post(self, request: Request) -> Response:  # type: ignore
        pass


class SignInAPI(APIView):
    @swagger_auto_schema(
        tags=["유저"],
        operation_summary="로그인",
        operation_description="로그인을 합니다.",
    )
    def post(self, request: Request) -> Response:  # type: ignore
        pass
