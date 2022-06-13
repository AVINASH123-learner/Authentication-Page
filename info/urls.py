from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('signup', views.signup, name="SignUp"),
    path('signin', views.signin, name="SignIn"),
    path('signout', views.signout, name="SignOut")
]
