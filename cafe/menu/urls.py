from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="menu_index"),
    path('manage/', index_manage, name="manage_index"),
    path('menu_list/', index_menu_list, name="menu_list_index"),
    path('create/', create_menu, name="menu_create"),
    path('<int:menu_id>/delete', delete_menu, name="menu_delete"),
    path('<int:menu_id>/update', update_menu, name="menu_update"),
    path('menu_type_list/', index_menu_type_list, name="menu_type_list_index"),
    path('menu_type_create/', create_menu_type, name="menu_type_create"),
    path('menu_type_delete/<int:menu_type_id>', delete_menu_type, name="menu_type_delete"),
    path('menu_type_update/<int:menu_type_id>', update_menu_type, name="menu_type_update"),
    path('order', index_order, name="order_index"),
    path('order_list', index_order_list, name="order_list_index"),
    # path('menu_type_delete/<int:menu_type_id>', )
]