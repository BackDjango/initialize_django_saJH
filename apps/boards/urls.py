from django.urls import path

from apps.boards.apis import BoardDetailAPI, BoardListAPI

urlpatterns = [
    path("", BoardListAPI.as_view(), name="board-list"),
    path("/<int:board_id>", BoardDetailAPI.as_view(), name="board-detail"),
]
