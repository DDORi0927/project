import json
from django.shortcuts import render, redirect, reverse
from .models import Menu, MenuType, OrderList

def index(request):
    list_menu = Menu.objects.all()
    print(list_menu)
    context = {"list_menu" : list_menu}
    dict_menu = {}
    for menu in list_menu:
        menu_type = menu.menu_type.name
        if not dict_menu.get(menu_type):
            dict_menu[menu_type] = []
        dict_menu[menu_type].append(menu)
    print(dict_menu)
    context = {"dict_menu" : dict_menu}
    return render(request, 'menu/index.html', context)

def index_manage(request):
    user_is_staff = request.user.is_staff
    print(user_is_staff)
    if user_is_staff:
        return render(request, 'menu/index_manage.html')
    return render(request, '404.html')

def index_menu_list(request):
    data_get_menu_type = request.GET.get("menu_type")
    list_menu = Menu.objects.filter(menu_type__menu_type = data_get_menu_type)
    list_menu_type = MenuType.objects.all()
    context = {"list_menu":list_menu, "menu_type":data_get_menu_type, "list_menu_type":list_menu_type}
    return render(request, 'menu/index_menu_list.html', context)

def create_menu(request):
    if request.method == "POST":
        data_post = request.POST
        print(data_post)
        print(request.FILES)
        print(reverse('menu_list_index'))
        Menu.objects.create(
            menu_type=data_post["menu_type"], name=data_post["name"], price=data_post["price"], image=request.FILES.get("image"))
        return redirect(reverse('menu_list_index')+"?menu_type=%s" % data_post["menu_type"])
    return render(request, 'menu/menu_create.html')

def delete_menu(request, menu_id):
    if request.method == "POST":
        obj_menu = Menu.objects.get(id=menu_id)
        obj_menu_type = obj_menu.menu_type
        obj_menu.image.delete(save=False)
        obj_menu.delete()
        return redirect(reverse('menu_list_index') + "?menu_type=%s" % obj_menu_type)

def update_menu(request, menu_id):
    obj_menu = Menu.objects.get(id=menu_id)
    print(obj_menu)
    context = {"obj_menu" : obj_menu}
    if request.method == "POST":
        data_post = request.POST
        obj_menu.menu_type = data_post["menu_type"]
        obj_menu.name = data_post["name"]
        obj_menu.price = data_post["price"]
        if request.FILES.get("image"):
            obj_menu.image.delete(save=False)
            obj_menu.image = request.FILES["image"]
        obj_menu.save()
        return redirect(reverse('menu_list_index') + "?menu_type=%s" % obj_menu.menu_type)

    return render(request, 'menu/menu_update.html', context)

def index_menu_type_list(request):
    obj_menu_type = MenuType.objects.all()
    context = {"obj_menu_type": obj_menu_type}
    return render(request, 'menu/index_menu_type_list.html', context)

def create_menu_type(request):
    if request.method == "POST":
        data_post = request.POST
        print(data_post)
        print("name", data_post["name"])
        print("type", data_post["type"])
        MenuType.objects.create(
            menu_type=data_post["type"], name=data_post["name"]
        )
    return redirect(reverse('menu_type_list_index'))

def delete_menu_type(request, menu_type_id):
    if request.method == "POST":
        print("menutype : ", menu_type_id)
        obj_menu = MenuType.objects.get(id=menu_type_id)
        obj_menu.delete()
    return redirect(reverse('menu_type_list_index'))

def update_menu_type(request, menu_type_id):
    if request.method == "POST":
        obj_menu_type = MenuType.objects.get(id=menu_type_id)
        data_post = request.POST
        print(data_post)
        obj_menu_type.menu_type = data_post["menu_type"]
        obj_menu_type.name = data_post["name"]
        obj_menu_type.save()

    return redirect(reverse('menu_type_list_index'))

def index_order(request):
    if request.method == "POST":
        post_data = request.POST
        print("aa", post_data)
        payment = int(post_data["payment"])
        input_order_menu = json.loads(post_data["input_order_menu"])
        print(type(payment), payment)
        print(type(input_order_menu), input_order_menu)

        for menu in input_order_menu.values():
            OrderList.objects.create(
                menu_type=menu["menu_type"], name=menu["name"], price=menu["price"], number=menu["num"], payment=payment)

    obj_menu = Menu.objects.all()
    print(obj_menu)
    context = {"obj_menu": obj_menu}
    return render(request, 'menu/index_order.html', context)

def index_order_list(request):
    obj_order = OrderList.objects.all()
    context = {"obj_order": obj_order}
    return render(request, 'menu/index_order_list.html', context)

    # list_menu = Menu.objects.all()
    # print(list_menu)
    # context = {"list_menu" : list_menu}
    # dict_menu = {}
    # for menu in list_menu:
    #     menu_type = menu.menu_type.name
    #     if not dict_menu.get(menu_type):
    #         dict_menu[menu_type] = []
    #     dict_menu[menu_type].append(menu)
    # print(dict_menu)
    # context = {"dict_menu" : dict_menu}