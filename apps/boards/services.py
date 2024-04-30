from apps.boards.models import Board
from apps.boards.selectors import BoardSelector
from apps.commons.exceptions import NotFoundException
from apps.commons.services import update_model


class BoardService:
    def create_board(self, title: str, content: str, author) -> Board:
        return Board.objects.create(title=title, content=content, author=author)

    def update_board(self, board_id: int, author, title: str, content: str) -> Board:
        board_selector = BoardSelector()
        board = board_selector.get_board_by_id_and_author(
            board_id=board_id,
            author=author,
        )

        if board is None:
            raise NotFoundException("게시글을 찾을 수 없습니다.")

        fields = ["title", "content"]
        data = {
            "title": title,
            "content": content,
        }

        board, has_updated = update_model(instance=board, fields=fields, data=data)
        return board

    def delete_board(self, board_id: int, author) -> bool:
        board_selector = BoardSelector()
        board = board_selector.get_board_by_id_and_author(
            board_id=board_id,
            author=author,
        )

        if board is None:
            raise NotFoundException("게시글을 찾을 수 없습니다.")

        board.delete()
        return True
