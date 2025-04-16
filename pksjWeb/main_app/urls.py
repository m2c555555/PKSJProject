from main_app import views
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('',views.index),
    path('accounts/', include('allauth.urls')),
    path('home/', views.home, name='home'),

]