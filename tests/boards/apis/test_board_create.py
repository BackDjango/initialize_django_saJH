import pytest
from django.urls import reverse

from tests.utils import IsAuthenticateTestCase

pytestmark = pytest.mark.django_db


class TestBoardCreate(IsAuthenticateTestCase):
    url = reverse("api-boards:board-list")

    def test_board_create_success(self, board):
        title = "test"
        content = "test"

        access_token = self.obtain_token(board.author)
        self.authenticate_with_token(access_token)
        response = self.client.post(
            path=self.url,
            data={
                "title": title,
                "content": content,
            },
            format="json",
        )

        assert response.status_code == 201
        assert response.data["data"]["title"] == title
        assert response.data["data"]["content"] == content
        assert response.data["data"]["author"] == board.author.email

    def test_board_create_fail_not_authenticated(self, board):
        response = self.client.post(self.url)

        assert response.status_code == 401
        assert response.data["code"] == "not_authenticated"
        assert response.data["message"] == "Authentication credentials were not provided."
