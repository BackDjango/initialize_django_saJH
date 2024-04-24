import pytest
from django.urls import reverse

from tests.utils import IsAuthenticateTestCase

pytestmark = pytest.mark.django_db


class TestBoardDelete(IsAuthenticateTestCase):
    def test_board_delete_success(self, board):
        access_token = self.obtain_token(board.author)
        self.authenticate_with_token(access_token)
        response = self.client.delete(
            path=reverse("api-boards:board-detail", kwargs={"board_id": board.id}),
        )

        assert response.status_code == 204

    def test_board_delete_fail_not_authenticated(self, board):
        response = self.client.delete(
            path=reverse("api-boards:board-detail", kwargs={"board_id": board.id}),
        )

        assert response.status_code == 401
        assert response.data["code"] == "not_authenticated"
        assert response.data["message"] == "Authentication credentials were not provided."
