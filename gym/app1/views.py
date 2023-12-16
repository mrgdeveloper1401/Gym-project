from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import *

# Create your views here.

#ویوی ثبت نام مدیر/باشگاه
class gymmanager_signupview(CreateView):
    model = Gym
    #فرمی که این ویو از آن استفاده میکند از چه نوعی است؟
    form_class = gymmanager_signupform
    #این ویو،برای نمایش این فرم کدام تمپلیت را استفاده میکند؟
    template_name = 'app1/templates/app1templates/gymmanager_signup.html'
    #
    def get_context_data(self,**kwargs):
        kwargs['user_type']= 'Gym'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('gymmanager-home')

#ویوی ثبت نام ورزشکار
class bodybuilder_signupview(CreateView):
    model = bodybuilder
    form_class = bodybuilder_signupform
    template_name = 'app1/templates/app1templates/bodybuilder_signup.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        kwargs['user_type']= 'bodybuilder'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('bodybuilder-home')

#ویوی لاگین کاربران
class loginview(auth_views.LoginView):
    form_class = loginform
    template_name = 'app1/templates/app1templates/login.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    
    def get_success_url(self) -> str:
        user = self.request.user
        if user.is_authenticated:
            if user.is_gymManager:
                return reverse('gymmanager-home')
            elif user.is_bodybuilder:
                return reverse('bodybuilder-home')
        else:
            return reverse('login')
