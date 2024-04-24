from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.apis.pagination import LimitOffsetPagination, get_paginated_data
from apps.apis.response import create_response
from apps.boards.selectors import BoardSelector
from apps.boards.services import BoardService
from apps.commons.base.serializers import BaseResponseSerializer, BaseSerializer
from apps.commons.exceptions import NotFoundException


class BoardListAPI(APIView):
    permission_classes = (IsAuthenticated,)

    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class FilterSerializer(BaseSerializer):
        keyword = serializers.CharField(required=False)
        limit = serializers.IntegerField(default=10, min_value=1, max_value=50)
        offset = serializers.IntegerField(default=0, min_value=0)

    class OutputSerializer(BaseSerializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        content = serializers.CharField()
        created_at = serializers.DateTimeField()
        author = serializers.CharField(source="author.email")

    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 목록 조회",
        operation_description="게시글 목록을 조회합니다.",
        query_serializer=FilterSerializer,
        responses={status.HTTP_200_OK: BaseResponseSerializer(data_serializer=OutputSerializer, pagination_serializer=True)},
    )
    def get(self, request: Request) -> Response:
        filter_serializer = self.FilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        board_selector = BoardSelector()
        boards = board_selector.get_board_list(filters=filter_serializer.validated_data)

        pagination_boards_data = get_paginated_data(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=boards,
            request=request,
            view=self,
        )
        return create_response(data=pagination_boards_data, status_code=status.HTTP_200_OK)

    class InputSerializer(BaseSerializer):
        title = serializers.CharField()
        content = serializers.CharField()

    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 작성",
        operation_description="게시글을 작성합니다.",
        request_body=InputSerializer,
    )
    def post(self, request: Request) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        board_sevice = BoardService()
        board = board_sevice.create_board(
            author=request.user,
            **input_serializer.validated_data,
        )

        output_serializer_data = self.OutputSerializer(board).data
        return create_response(data=output_serializer_data, status_code=status.HTTP_201_CREATED)


class BoardDetailAPI(APIView):
    permission_classes = (IsAuthenticated,)

    class OutputSerializer(BaseSerializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        content = serializers.CharField()
        created_at = serializers.DateTimeField()
        updated_at = serializers.DateTimeField()
        author = serializers.CharField(source="author.email")

    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 상세 조회",
        operation_description="게시글을 조회합니다.",
        responses={status.HTTP_200_OK: BaseResponseSerializer(data_serializer=OutputSerializer)},
    )
    def get(self, request: Request, board_id: int) -> Response:
        board_selector = BoardSelector()
        board = board_selector.get_board_by_id(board_id=board_id)

        if board is None:
            raise NotFoundException("게시글을 찾을 수 없습니다.")

        output_serializer_data = self.OutputSerializer(board).data
        return create_response(data=output_serializer_data, status_code=status.HTTP_200_OK)

    class InputSerializer(BaseSerializer):
        title = serializers.CharField(required=True, max_length=32)
        content = serializers.CharField(required=False, max_length=512)

    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 수정",
        request_body=InputSerializer,
        operation_description="게시글을 수정합니다.",
        responses={status.HTTP_200_OK: BaseResponseSerializer(data_serializer=OutputSerializer)},
    )
    def put(self, request: Request, board_id: int) -> Response:
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        board_service = BoardService()
        board = board_service.update_board(
            board_id=board_id,
            author=request.user,
            **input_serializer.validated_data,
        )

        output_serializer_data = self.OutputSerializer(board).data
        return create_response(data=output_serializer_data, status_code=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 삭제",
        operation_description="게시글을 삭제합니다.",
    )
    def delete(self, request: Request, board_id: int) -> Response:
        board_service = BoardService()
        board_service.delete_board(board_id=board_id, author=request.user)

        return create_response(status_code=status.HTTP_204_NO_CONTENT)
