from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
admin.site.register(custom_user)
admin.site.register(bodybuilder)
admin.site.register(Gym)
admin.site.register(work_time)
admin.site.register(damage)
admin.site.register(movements)
admin.site.register(coach)
admin.site.register(crew)
admin.site.register(Agreement)
admin.site.register(program)
admin.site.register(Membership)
admin.site.register(Reserve)

