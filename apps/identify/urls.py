from django.urls import path
# 子路由

from django.urls import path
from . import views

urlpatterns = [
    path('imagefile/',views.IdentifyBankView.as_view()),
]