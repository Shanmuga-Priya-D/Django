from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
]