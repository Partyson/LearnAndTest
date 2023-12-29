from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tests/', views.library),
    path('test-creator/', views.test_crator),
    path('workshop/', views.mastery),
    path('test/', views.test)
]