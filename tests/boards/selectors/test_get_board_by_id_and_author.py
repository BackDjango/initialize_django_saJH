import pytest

from apps.boards.selectors import BoardSelector

pytestmark = pytest.mark.django_db


class TestGetBoardByIdAndAuthor:
    def setup_method(self):
        self._board_selector = BoardSelector()

    def test_get_board_by_id_and_author_success(self, board):
        board_instance = self._board_selector.get_board_by_id_and_author(board.id, board.author)

        assert board_instance == board

    def test_get_board_by_id_and_author_fail(self):
        board_instance = self._board_selector.get_board_by_id_and_author(1, 1)

        assert board_instance is None
