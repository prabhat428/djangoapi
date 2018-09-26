"""uc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/<int:pk>/',views.userDetail.as_view()),
    path('users/',views.userList.as_view()),
    path('check/',views.checkUser.kaaroFunction, name='kaaro FUnction'),
    path('register/',views.registerUser.register, name='Register'),
    path('mailcheck/',views.mailCheck.send_email, name='Email Check'),
    path('data/',views.dataplay.getusersdata, name='Data Play')
]
