
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

handler404 = 'main.views.handler404'

handler500 = 'main.views.handler500'