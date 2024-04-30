import pytest
from django.urls import reverse

from tests.utils import IsAuthenticateTestCase

pytestmark = pytest.mark.django_db


class TestBoardDetail(IsAuthenticateTestCase):
    def test_board_detail_success(self, board):
        access_token = self.obtain_token(board.author)
        self.authenticate_with_token(access_token)
        response = self.client.get(
            path=reverse("api-boards:board-detail", kwargs={"board_id": board.id}),
        )

        assert response.status_code == 200
        assert response.data["data"]["id"] == board.id
        assert response.data["data"]["title"] == board.title
        assert response.data["data"]["content"] == board.content

    def test_board_detail_fail_board_not_found(self, board):
        access_token = self.obtain_token(board.author)
        self.authenticate_with_token(access_token)
        response = self.client.get(
            path=reverse("api-boards:board-detail", kwargs={"board_id": 999}),
        )

        assert response.status_code == 404
        assert response.data["code"] == "not_found"
        assert response.data["message"] == "게시글을 찾을 수 없습니다."

    def test_board_detail_fail_not_authenticated(self, board):
        response = self.client.get(
            path=reverse("api-boards:board-detail", kwargs={"board_id": board.id}),
        )

        assert response.status_code == 401
        assert response.data["code"] == "not_authenticated"
        assert response.data["message"] == "Authentication credentials were not provided."
