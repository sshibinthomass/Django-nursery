from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.catalogue,name='catalogue'),
    path('changeval', views.changeVal,name='changeVal'),
]
