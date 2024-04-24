from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class BoardListAPI(APIView):
    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 목록 조회",
        operation_description="게시글 목록을 조회합니다.",
    )
    def get(self, request: Request) -> Response:  # type: ignore
        pass

    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 작성",
        operation_description="게시글을 작성합니다.",
    )
    def post(self, request: Request) -> Response:  # type: ignore
        pass


class BoardDetailAPI(APIView):
    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 상세 조회",
        operation_description="게시글을 조회합니다.",
    )
    def get(self, request: Request, board_id: int) -> Response:  # type: ignore
        pass

    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 수정",
        operation_description="게시글을 수정합니다.",
    )
    def put(self, request: Request, board_id: int) -> Response:  # type: ignore
        pass

    @swagger_auto_schema(
        tags=["게시판"],
        operation_summary="게시글 삭제",
        operation_description="게시글을 삭제합니다.",
    )
    def delete(self, request: Request, board_id: int) -> Response:  # type: ignore
        pass
