
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signin/', views.signin_view, name='signin'),
    path('account/', views.account, name='account'),
    path('request_password_reset/', views.request_password_reset, name='request_password_reset'),
    path('reset_password/<token>', views.reset_password, name='reset_password'),
]
