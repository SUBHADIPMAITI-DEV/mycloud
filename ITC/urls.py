
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
import os
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    # path('index',views.index,name="index"),
    path('upload',views.home,name="upload"),

    # path('upload', views.upload_file, name='upload'),
    # path('download/<str:file_name>/', views.download_file, name='download'),
]



# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)