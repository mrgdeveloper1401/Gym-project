from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

admin.site.register(bodybuilder)
admin.site.register(Gym)
admin.site.register(custom_user)
admin.site.register(work_time)
admin.site.register(damage)