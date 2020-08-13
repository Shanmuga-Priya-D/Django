from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('search',views.search,name='search'),
    path('book',views.book,name='book'),
    path('myprofile',views.myprofile,name='myprofile'),
    path('confirm',views.confirm,name='confirm'),
    path('update_item/',views.updateItem,name='update_item'),
    path('mybookings',views.mybookings,name='mybookings'),
    path('login', views.LoginView.as_view(), name='login'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    
]