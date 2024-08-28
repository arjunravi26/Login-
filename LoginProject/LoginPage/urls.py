
from django.contrib import admin
from django.urls import path
from LoginPage import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.home, name='home'),
    path('logout', views.logout_user, name='logout')
]
