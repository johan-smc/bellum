from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register),
    path('token/', views.obtain_expiring_auth_token),
    path('get_users/', views.get_users),
    path('register_group/', views.register_group),
    path('get_groups/', views.get_groups),
    path('del_group/', views.del_group),
    path('usr_to_group/', views.usr_to_group),
    path('upload_file/', views.upload_file),
    path('del_file/', views.del_file),
    path('create_folder/', views.create_folder),
    path('update_file/', views.update_file),
    path('inode_to_user/', views.inode_user),
    path('inode_to_group/', views.inode_group),
    path('get_inodes/', views.get_inodes),
    path('get_inodes_group/', views.get_inodes_group),
    path('get_all_groups/',views.get_all_groups),
    path('get_usrid/',views.get_usrid),
    path('get_groups_owner/',views.get_groups_owner),
    path('get_file/', views.get_file),
    path('update_pass/', views.update_pass),
    path('get_all_user/', views.get_all_user),
]
