"""
URL configuration for django_vue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# 总路由添加路由转换器
from utils.converters import UsernameConverter,MobileConverter
from django.urls import register_converter

register_converter(UsernameConverter,'username')
register_converter(MobileConverter,'mobile')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('apps.users.urls')),#添加分路由，上面有解释用法
    path('',include('apps.identify.urls')),#身份验证的路由
    path('',include('apps.yolo.urls')),#yolov8检测的路由
]
