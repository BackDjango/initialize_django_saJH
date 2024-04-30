import pytest

from apps.boards.services import BoardService
from apps.commons.exceptions import NotFoundException

pytestmark = pytest.mark.django_db


class TestUpdateBoard:
    def setup_method(self):
        self._board_service = BoardService()

    def test_update_board_success(self, board):
        title = "test"
        content = "test"
        updated_board = self._board_service.update_board(
            board_id=board.id,
            title=title,
            content=content,
            author=board.author,
        )

        assert updated_board.title == title
        assert updated_board.content == content
        assert updated_board.author == board.author

    def test_update_board_fail(self, active_user):
        title = "test"
        content = "test"

        with pytest.raises(NotFoundException) as e:
            self._board_service.update_board(
                board_id=1,
                title=title,
                content=content,
                author=active_user,
            )

        assert str(e.value) == "게시글을 찾을 수 없습니다."
        assert isinstance(e.value, NotFoundException)
