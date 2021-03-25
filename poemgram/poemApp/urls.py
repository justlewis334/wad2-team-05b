from django.contrib import admin
from django.urls import path
from django.urls import include
from poemApp import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
]
