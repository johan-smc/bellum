from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register),
    path('token/', views.obtain_expiring_auth_token)
]