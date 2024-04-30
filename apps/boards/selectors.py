from typing import Optional

from django.db.models.query import QuerySet

from apps.boards.filters import BoardFilter
from apps.boards.models import Board


class BoardSelector:
    def get_board_list(self, filters: Optional[dict]) -> QuerySet[Board]:
        filters = filters or {}
        qs = Board.objects.select_related("author").all()
        return BoardFilter(filters, qs).qs

    def check_is_exists_board_by_id_and_author(self, board_id: int, author) -> bool:
        return Board.objects.filter(id=board_id, author=author).exists()

    def get_board_by_id(self, board_id: int) -> Optional[Board]:
        try:
            return Board.objects.get(id=board_id)

        except Board.DoesNotExist:
            return None

    def get_board_by_id_and_author(self, board_id: int, author) -> Optional[Board]:
        try:
            return Board.objects.get(id=board_id, author=author)

        except Board.DoesNotExist:
            return None
