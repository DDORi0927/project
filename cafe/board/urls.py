from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="board_index"),
    path('<int:board_id>', read_board, name="board_read"),
    path('<int:board_id>/update', update_board, name="board_update"),
    path('<int:board_id>/delete', delete_board, name="board_delete"),
    path('create/', create_board, name="board_create"),
    path('<int:board_id>/create_reply', create_reply, name="reply_create"),
    path('<int:board_id>/create_replay/<int:reply_id>', delete_reply, name="reply_delete"),
    path('<int:board_id>/update_reply/<int:reply_id>', update_reply, name="reply_update"),
    path('int:board_id/create_good/<int:create_good>', create_good, name="good_create"),
]