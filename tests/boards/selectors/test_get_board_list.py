import pytest

from apps.boards.selectors import BoardSelector

pytestmark = pytest.mark.django_db


class TestGetBoardList:
    def setup_method(self):
        self._board_selector = BoardSelector()

    def test_get_board_list_success(self, board):
        board_list = self._board_selector.get_board_list({})

        assert board_list.count() == 1
        assert board_list.first() == board

    def test_get_board_list_success_filter(self, board):
        filters = {
            "title": board.title,
        }
        board_list = self._board_selector.get_board_list(filters)

        assert board_list.count() == 1
        assert board_list.first() == board
