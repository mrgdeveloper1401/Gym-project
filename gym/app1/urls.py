from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.bodybuilder_home,name='=bodybuilder-home'),
    path('gymmanger/',views.gymmanager_home,name = 'gymmanager-home'),
    path('login/', views.loginview.as_view(),name='login'),
    path('signup/bodybuilder/',views.bodybuilder_signupview.as_view(),name = 'bodybuilder-signup'),
    path('signup/gymmanager/',views.gymmanager_signupview.as_view(),name = 'gymmanager-signup'),
    path('logout/',auth_views.LogoutView.as_view(template_name='app1templates/logout.html'),name ='logout'),
    path('bodybuilder/damage/create/',views.create_damage,name='create-damage'),
    path('gymmanager/worktime/create/',views.create_worktime,name='create-worktime'),

]