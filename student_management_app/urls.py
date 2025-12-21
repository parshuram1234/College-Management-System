from django.contrib import admin
from django.urls import path, include
from student_management_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginUser, name="login"),
    #path('logout_user', views.logout_user, name="logout_user"),
    #path('registration', views.registration, name="registration"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('doRegistration', views.doRegistration, name="doRegistration"),
]
