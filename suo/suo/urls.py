from django.contrib import admin
from django.urls import path, include #importamo include
from main import views

urlpatterns = [

    path('', views.homepage),
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
]


print(f'URL patterns: {urlpatterns}')