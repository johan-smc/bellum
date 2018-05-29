from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register),
    path('token/', views.obtain_expiring_auth_token),
    path('get_users/', views.get_users),
    path('register_group/', views.register_group),
    path('get_groups/', views.get_groups),
    path('del_group/', views.del_group),
    path('usr_to_group/', views.usr_to_group)


]
