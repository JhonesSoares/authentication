from django.urls import path
from django.contrib import admin

from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('user_update/', views.user_update, name='user_update'),
    path('user_delete/', views.user_delete, name='user_delete'),
]    