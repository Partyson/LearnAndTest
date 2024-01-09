from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tests/', views.library),
    path('test-creator/', views.test_creator),
    path('workshop/', views.mastery),
    path('test/', views.test),
    path('register/', views.register),
    path('login/', views.login)
]