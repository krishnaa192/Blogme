from django.contrib import admin
from django.urls import path
from . import views

# app_name='blogging'

urlpatterns = [
    path("", views.Home, name="Home"),
    path('authors/', views.authors, name="authors"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signup/', views.signup, name="signup"),
    path('Read/<str:pk>/', views.Read, name="Read"),
]
