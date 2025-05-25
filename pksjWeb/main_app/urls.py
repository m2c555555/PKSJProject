from main_app import views
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('profile/', views.profile, name='profile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)