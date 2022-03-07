from django.contrib import admin
from django.urls import path, include
from .views import motest_datail_view


app_name = 'motest'

urlpatterns = [
    path('<int:pk>/', motest_datail_view, name='motest_detail'),
    path('<slug:slug>/', motest_datail_view, name='motest_detail_slug')
]