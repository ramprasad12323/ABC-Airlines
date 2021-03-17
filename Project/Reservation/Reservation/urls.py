"""Reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import regist_user,login, validation, register, inv_pass, user_notpresent, bookticket, viewticket, book, user_there, sucess_reg,home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login),
    path('registration/', regist_user),
    path('invpass/', inv_pass),
    path('usernotpresent/', user_notpresent),
    path('userpresent/', user_there),
    path('sucessreg/', sucess_reg),
    path('bookticket/', bookticket),

    path('viewticket/', viewticket),
    path('validation/', validation),
    path('register/', register),
    path('book/', book),
]
