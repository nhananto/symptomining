
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url, handler404, handler500
# from django.conf import settings
# from django.views.static import serve 

urlpatterns = [
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]

handler404 = 'main.views.handler404'

handler500 = 'main.views.handler500'