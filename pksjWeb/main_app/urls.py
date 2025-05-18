from main_app import views
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index),
    path('profile/', views.profile, name='profile'),

]