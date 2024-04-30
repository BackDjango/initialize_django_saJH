import pytest

from apps.boards.services import BoardService
from apps.commons.exceptions import NotFoundException

pytestmark = pytest.mark.django_db


class TestDeleteBoard:
    def setup_method(self):
        self._board_service = BoardService()

    def test_delete_board_success(self, board):
        is_deleted = self._board_service.delete_board(board.id, board.author)

        assert is_deleted is True

    def test_delete_board_fail(self, active_user):
        with pytest.raises(NotFoundException) as e:
            self._board_service.delete_board(1, active_user)

        assert str(e.value) == "게시글을 찾을 수 없습니다."
        assert isinstance(e.value, NotFoundException)
