from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_view

app_name = 'acct'

urlpatterns = [
    path('', customer_login, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='acct/logout.html'), name='logout'),
]