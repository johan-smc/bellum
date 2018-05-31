from bellum_app.models import My_User
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def get_users():
    return User.objects.all()

def get_myuser(pk):
    var = My_User.objects.filter(id=pk)[0]
    print("---->" , var)
    return var

def get_pk(token):
    token = Token.objects.get(key=token)
    user = User.objects.get(id = token.user_id)
    print("-------------------------------------......................--------------->",user.my_user)
    return user.my_user.id

def get_groups(mi_user):
    return mi_user.groups.all()

def get_last(user):
    return user.password_change