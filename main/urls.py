from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checkup/', views.checkup, name='checkup'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),



]