from bellum_app.models import My_User
from django.contrib.auth.models import User

def get_users():
    return User.objects.all()