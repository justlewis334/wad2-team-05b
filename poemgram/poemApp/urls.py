from django.contrib import admin
from django.urls import path
from django.urls import include
from poemApp import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('validate/', views.checkUserName, name='validate'),
    path('user/<slug:usernameSlug>', views.showUserprofile, name='showUserprofile'),
    path('search/', views.search, name='search'),
    path('compose/', views.compose, name='compose'),
    path('submitPoem/', views.submitPoem, name='submitPoem'),
    path('precompose/', views.preCompose, name='precompose'),
    path('like/', views.poem_like_unlike, name='like-poem'),
]
