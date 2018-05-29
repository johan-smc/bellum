from django.contrib import admin
from .models import *

admin.site.register(My_user);
admin.site.register(Group);
admin.site.register(INode);
admin.site.register(Role);

# Register your models here.
