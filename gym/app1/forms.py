from typing import Any
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db import transaction
from .models import custom_user,Gym,bodybuilder,damage
from django import forms
from django.contrib.auth import get_user_model

user = get_user_model()

#فرم برای ثبت نام مدیر/باشگاه
class gymmanager_signupform(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    gymmanager_fullname = forms.CharField(widget=forms.TextInput())
    gym_name = forms.CharField(widget=forms.TextInput())
   # workingtime=
    manager_cv = forms.CharField(widget=forms.Textarea())
    #manager_password = models.CharField(max_length=15)
    facilities = forms.CharField(widget=forms.Textarea())
    capacity = forms.IntegerField(widget=forms.NumberInput())
    numberofmachines = forms.IntegerField(widget=forms.NumberInput())
   # numberofworkers=
    foundationdate = forms.DateField(widget=forms.DateInput())
   # address=
    #tuition =
    #phonenumber
    class Meta(UserCreationForm.Meta):
        model = custom_user
        fields = ('user_name','email','password1','password2')

    @transaction.Atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_gymManager = True
        if commit:
            user.save()
        gymmanager = Gym.objects.create(
            user=user,
            gymmanager_fullname=self.cleaned_data.get('gymmanager_fullname'),
            gym_name=self.cleaned_data.get('gym_name'),
            #workingtime
            manager_cv=self.cleaned_data.get('manager_cv'),
            #manager_password
            facilities=self.cleaned_data.get('facilities'),
            capacity= self.cleaned_data.get('capacity'),
            numberofmachines=self.cleaned_data.get('numberofmachines'),
            # numberofworkers=
            foundationdate = self.cleaned_data.get('foundationdate'),
            # address=
            #tuition =
            #phonenumber
        )
        return 





#فرم برای ثبت نام ورزشکار
#فرم برای لاگین مدیر/باشگاه
#فرم برای لاگین ورزشکار