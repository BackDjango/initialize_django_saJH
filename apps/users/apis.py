from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenRefreshView

from apps.apis.response import create_response
from apps.commons.base.serializers import BaseResponseSerializer, BaseSerializer
from apps.commons.exceptions import InvalidTokenException
from apps.users.services import UserService


class SignUpAPI(APIView):
    class InputSerializer(BaseSerializer):
        email = serializers.EmailField(required=True, max_length=255)
        password = serializers.CharField(required=True, max_length=128)
        username = serializers.CharField(required=True, max_length=16)

    class OutputSerializer(BaseSerializer):
        id = serializers.IntegerField()
        email = serializers.EmailField()
        username = serializers.CharField()
        created_at = serializers.DateTimeField()

    @swagger_auto_schema(
        tags=["유저"],
        operation_summary="회원가입",
        operation_description="회원가입을 합니다.",
        request_body=InputSerializer,
        responses={
            status.HTTP_200_OK: BaseResponseSerializer(data_serializer=OutputSerializer),
        },
    )
    def post(self, request: Request) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        user_service = UserService()
        user = user_service.create_user(**input_serializer.validated_data)

        output_serializer_data = self.OutputSerializer(user).data
        return create_response(data=output_serializer_data, status_code=status.HTTP_201_CREATED)


class SignInAPI(APIView):
    class InputSerializer(BaseSerializer):
        username = serializers.CharField(required=True, max_length=16)
        password = serializers.CharField(required=True, max_length=128)

    class OutputSerializer(BaseSerializer):
        access_token = serializers.CharField()
        refresh_token = serializers.CharField()

    @swagger_auto_schema(
        tags=["유저"],
        operation_summary="로그인",
        operation_description="로그인을 합니다.",
        request_body=InputSerializer,
        responses={
            status.HTTP_200_OK: BaseResponseSerializer(data_serializer=OutputSerializer),
        },
    )
    def post(self, request: Request) -> Response:  # type: ignore
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        user_service = UserService()
        tokens = user_service.sign_in(**input_serializer.validated_data)

        output_serializer_data = self.OutputSerializer(tokens).data
        return create_response(data=output_serializer_data, status_code=status.HTTP_200_OK)


class RefreshTokenAPI(TokenRefreshView):
    class InputSerializer(BaseSerializer):
        refresh_token = serializers.CharField(required=True, max_length=128)

    class OutputSerializer(BaseSerializer):
        access_token = serializers.CharField()
        refresh_token = serializers.CharField()

    @swagger_auto_schema(
        tags=["유저"],
        operation_summary="토큰 갱신",
        operation_description="토큰을 갱신합니다.",
        request_body=InputSerializer,
        responses={
            status.HTTP_200_OK: BaseResponseSerializer(data_serializer=OutputSerializer),
        },
    )
    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError:
            raise InvalidTokenException("토큰이 만료 또는 유효하지 않습니다.")

        output_serializer_data = self.OutputSerializer({"access_token": serializer.validated_data["access"]}).data
        return create_response(data=output_serializer_data, status_code=status.HTTP_200_OK)
