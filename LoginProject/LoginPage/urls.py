
from django.contrib import admin
from django.urls import path
from LoginPage import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logout_user, name='logout')
]
