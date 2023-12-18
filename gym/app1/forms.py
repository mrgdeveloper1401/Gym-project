from typing import Any
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db import transaction
from django.db.models.base import Model
from .models import *
from django import forms
from django.contrib.auth import get_user_model

user = get_user_model()

#فرم برای ثبت نام مدیر/باشگاه
class gymmanager_signupform(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    gymmanager_fullname = forms.CharField(widget=forms.Textarea())
    gym_name = forms.CharField(widget=forms.TextInput(),max_length=20)
   # workingtime=
    manager_cv = forms.CharField(widget=forms.Textarea())
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
        #user = super().save(commit=False)
        user.is_gymManager = True
       # if commit:
          #  user.save()
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
        return user
# ساخت فیلد (ولیبل) سفارشی برای انتخاب آسیب ها در فرم ثبت نام ورزشکار
class custom_modelmultiplechoicefield(forms.ModelMultipleChoiceField):
    def label_from_instance(self, damage) -> str:
        return "%s" %damage.what
    
#فرم برای ثبت نام ورزشکار
class bodybuilder_signupform(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    firstname = forms.CharField(widget=forms.TextInput(),max_length=15)
    lastname = forms.CharField(widget=forms.TextInput(),max_length=15)
    gender = forms.ChoiceField (widget=forms.Select(),choices=Gender.choices)
    height = forms.IntegerField(widget=forms.NumberInput())
    weight = forms.IntegerField(widget=forms.NumberInput())
    nationalcode = forms.IntegerField(widget=forms.NumberInput())
    phonenumber = forms.IntegerField(widget=forms.NumberInput())
    aim = forms.CharField(widget=forms.Textarea())
    #illness = forms.CharField(widget=forms.te)
    birthdate = forms.DateField(widget=forms.SelectDateWidget())
   # age = 
    damage = custom_modelmultiplechoicefield(
        queryset=damage.objects.all(),
        widget = forms.CheckboxSelectMultiple
        )

    class Meta(UserCreationForm.Meta):
        model = custom_user
        fields = ('user_name','email','password1','password2')

    @transaction.Atomic
    def save(self, commit=True):
        #user = super().save(commit=False)
        user.is_bodybuilder = True
        #if commit:
            #user.save()
        bodybuilder = bodybuilder.objects.create(
            user=user,
            firstname=self.cleaned_data.get('firstname'),
            lastname=self.cleaned_data.get('lastname'),
            gender=self.cleaned_data.get('gender'),
            height=self.cleaned_data.get('height'),
            weight= self.cleaned_data.get('weight'),
            nationalcode=self.cleaned_data.get('nationalcode'),
            phonenumber = self.cleaned_data.get('phonenumber'),
            aim = self.cleaned_data.get('aim'),
            #illness
            birthdate = self.cleaned_data.get('birthdate')
            #age
            #damage
        )
        return user
    

#فرم برای لاگین مدیر/باشگاه و ورزشکار
class loginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

#فرم برای افزودن آسیب به آسیب های ثبت شده
class damageform(forms.ModelForm):
    body_part = forms.CharField(max_length=20,widget=forms.TextInput())
    what = forms.CharField(max_length=100,widget=forms.Textarea())
    when = forms.ChoiceField(widget=forms.Select(choices=damagedwhen.choices))

    class Meta:
        model = damage
        fields = ('body_part','what')

    def save(self, commit=True):
        return super().save(commit)

#فرم برای افزودن ورک تایم به ورکتایم های ثبت شده
class work_timeform(forms.ModelForm):
    day = forms.ChoiceField(widget=forms.Select(choices=weekdays.choices))
    start = forms.TimeField(widget=forms.TimeInput())
    end = forms.TimeField(widget=forms.TimeInput())
    coach_crew = forms.ChoiceField(widget=forms.Select(choices=who_works.choices))

    class Meta:
        model = work_time
        fields = ('day','coach_crew','start')
    
    def save(self, commit=True) -> Any:
        return super().save(commit)