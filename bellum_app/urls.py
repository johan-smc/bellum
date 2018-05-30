from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register),
    path('token/', views.obtain_expiring_auth_token),
    path('get_users/', views.get_users),
    path('upload_file/', views.upload_file),
    path('del_file/',views.del_file),
    path('create_folder/', views.create_folder),
    path('update_file/', views.update_file)
]