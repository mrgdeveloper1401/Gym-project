from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Manager_CustomUser


class Manager_CustomUser_CreationForm(UserCreationForm):
    class meta:
        model = Manager_CustomUser
        fields = ("username","email")

class Manager_CustomUser_ChangeForm(UserChangeForm):

    class Meta:
        model = Manager_CustomUser
        fields = ("username", "email")

