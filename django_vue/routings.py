from django.urls import re_path
from yolo import consumers

websocket_urlpatterns = {
    re_path(r'text_video/',consumers.VideoConsumer.as_asgi()),
    re_path(r'file_video/',consumers.VideoFileConsumer.as_asgi()),
    re_path(r'camera_video/', consumers.VideoCameraConsumer.as_asgi()),
}