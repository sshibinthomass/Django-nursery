from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('plantfinder', views.plantfinder,name='plantfinder'),
    path('plantlist',views.plantlist,name='plantlist'),
]
