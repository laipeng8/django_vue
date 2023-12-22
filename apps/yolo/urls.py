from django.urls import path
from django_vue import settings
# 子路由

from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('yolo_image/',views.yoloDetectImage.as_view()),
    path('camera/',views.yoloDetectImage.as_view()),
    path('yolo_video/',views.yoloDetectVedio.as_view()),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







