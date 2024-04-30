import pytest
from django.urls import reverse

from tests.utils import IsAuthenticateTestCase

pytestmark = pytest.mark.django_db


class TestBoardList(IsAuthenticateTestCase):
    url = reverse("api-boards:board-list")

    def test_board_list_success(self, board):
        access_token = self.obtain_token(board.author)
        self.authenticate_with_token(access_token)
        response = self.client.get(
            path=self.url,
            data={
                "limit": 10,
                "offset": 0,
            },
        )
        assert response.status_code == 200
        assert response.data["data"]["count"] == 1
        assert response.data["data"]["results"][0]["id"] == board.id
        assert response.data["data"]["results"][0]["title"] == board.title
        assert response.data["data"]["results"][0]["content"] == board.content

    def test_board_list_fail_not_authenticated(self, board):
        response = self.client.get(self.url)

        assert response.status_code == 401
        assert response.data["code"] == "not_authenticated"
        assert response.data["message"] == "Authentication credentials were not provided."
