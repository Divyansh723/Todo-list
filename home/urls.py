from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login' , views.login, name='login'),
    path('register' , views.register, name='register'),
    path('Task', views.task, name='task'),
    path('delete/<slug>', views.DeleteTask, name='delete'),
    path('update/<slug>', views.Update, name='update'),
    path('logout', views.logout, name='logout'),
]