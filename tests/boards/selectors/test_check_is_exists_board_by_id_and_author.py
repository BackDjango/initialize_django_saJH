import pytest

from apps.boards.selectors import BoardSelector

pytestmark = pytest.mark.django_db


class TestCheckIsExistsBoardByIdAndAuthor:
    def setup_method(self):
        self._board_selector = BoardSelector()

    def test_check_is_exists_board_by_id_and_author_success(self, board):
        is_exist = self._board_selector.check_is_exists_board_by_id_and_author(board.id, board.author)

        assert is_exist is True

    def test_check_is_exists_board_by_id_and_author_fail(self):
        is_exist = self._board_selector.check_is_exists_board_by_id_and_author(1, 1)

        assert is_exist is False
