from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manager_CustomUser
from .forms import Manager_CustomUser_CreationForm, Manager_CustomUser_ChangeForm

# Register your models here.
class Manager_CustomUser_Admin(UserAdmin):
    add_form = Manager_CustomUser_CreationForm
    form = Manager_CustomUser_ChangeForm
    model = Manager_CustomUser
    list_display = ["username", "email"]

admin.site.register(Manager_CustomUser, Manager_CustomUser_Admin)