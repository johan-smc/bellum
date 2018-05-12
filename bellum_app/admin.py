from django.contrib import admin
from .models import *

admin.site.register(User);
admin.site.register(Group);
admin.site.register(Object);
admin.site.register(Role);
admin.site.register(Log);

# Register your models here.
