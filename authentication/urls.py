from django.urls import path
from django.contrib import admin

from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
]    