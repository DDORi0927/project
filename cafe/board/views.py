from django.shortcuts import render, redirect
from .models import Board, Reply, Good
from django.db.models import Q

def index(request):
    data_get_category = request.GET.get('category')
    if data_get_category == "free" or data_get_category == "question":
        list_board = Board.objects.filter(category=data_get_category)
    else:
        list_board = Board.objects.all()
    print(request.GET)
    print(request.GET.get("q"))
    data_get_query = request.GET.get("q")
    if data_get_query:
        list_board = Board.objects.filter(Q(title__contains=data_get_query) | Q(content__contains=data_get_query))
    context = {"list_board":list_board}

    return render(request, 'board/index.html', context)

def read_board(request, board_id):
    obj_board = Board.objects.get(id=board_id)
    obj_reply = Reply.objects.filter(board_id=board_id)
    print(obj_reply)
    context = {"obj_board" : obj_board, "obj_reply" : obj_reply}
    return  render(request, 'board/read_board.html', context)

def create_board(request):
    if request.method == "POST":
        data_post = request.POST
        user = request.user.username
        Board.objects.create(
            category=data_post["category"],
            title=data_post["title"],
            content=data_post["content"],
            writer=user
        )
        return redirect('board_index')
    return render(request, 'board/board_create.html')

def update_board(request, board_id):
    obj_board = Board.objects.get(id=board_id)
    context = {"obj_board" : obj_board}

    if request.method == "POST":
        data_post = request.POST
        obj_board.category = data_post["category"]
        obj_board.title = data_post["title"]
        obj_board.content = data_post["content"]
        obj_board.save()
        return redirect('board_index')

    return render(request, 'board/board_update.html', context)

def delete_board(request, board_id):
    obj_board = Board.objects.get(id=board_id)
    context = {"obj_board" : obj_board}
    if request.method == "POST":
        data_post = request.POST
        if data_post["delete"] == "Delete":
            obj_board.delete()
            return redirect('board_index')
        print(data_post)

    return render(request, 'board/board_delete.html', context)

def create_reply(request, board_id):
    if request.method == "POST":
        data_post = request.POST
        user = request.user.username
        Reply.objects.create(board_id=board_id, content=data_post["content"], writer=user)
        return redirect ('board_read', board_id=board_id)

def delete_reply(request, board_id, reply_id):
    if request.method == "POST":
        Reply.objects.get(id=reply_id).delete()
        return redirect('board_read', board_id=board_id)

def update_reply(request, board_id, reply_id):
    if request.method == "POST":
        obj_reply = Reply.objects.get(id=reply_id)
        data_post = request.POST
        obj_reply.content = data_post["content"]
        obj_reply.save()
        return redirect('board_read', board_id=board_id)

def create_good(request, board_id):
    if request.method == "POST":
        data_post = request.POST
        user = request.user.username
        Good.objects.create(board_id=board_id, writer=user)
        return redirect('board_read', board_id=board_id)
    # elif
# Create your views here.
