from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signin', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name="handlelogout"),
    path('users', views.users, name="users"),
    path("add", views.add, name="add"),
    path("name/<str:name>", views.nam, name="name"),
    path("send", views.send, name="send"),
   
]