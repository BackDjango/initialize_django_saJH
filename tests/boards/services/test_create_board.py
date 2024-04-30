import pytest

from apps.boards.services import BoardService

pytestmark = pytest.mark.django_db


class TestCreateBoard:
    def setup_method(self):
        self._board_service = BoardService()

    def test_create_board_success(self, active_user):
        title = "test"
        content = "test"
        board = self._board_service.create_board(title=title, content=content, author=active_user)

        assert board.title == title
        assert board.content == content
        assert board.author == active_user
