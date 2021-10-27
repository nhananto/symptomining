from django.urls import path
from main import views
from django.conf import settings
from django.views.static import serve 

urlpatterns = [
    #url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('', views.home, name='home'),
    path('checkup/', views.checkup, name='checkup'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),

]

