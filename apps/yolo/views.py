from django.shortcuts import render
import os
from utils.yolov8_detect import Detect
# Create your views here.
from django.views import View
from django.http import JsonResponse,StreamingHttpResponse,FileResponse
from wsgiref.util import FileWrapper
import base64
import shutil
from ultralytics import YOLO
import cv2
from utils.yolov8_detect import Detect

model = YOLO('D:/Django_project/django_vue_exam/django_vue/utils/weights/yolov8s.pt')

class yoloDetectImage(View):
    def get(self,request):
        try:
            # 删除之前存放检测图片的文件夹
            path = r'D:\Django_project\django_vue_exam\django_vue\runs'
            shutil.rmtree(path)
        except:
            pass
        image_url = request.GET.get('image_url')
        detector = Detect()#实例化utile中的图片检测方法
        image_url_save=detector.get_image_result(image_url)
        image_folder = fr'D:\Django_project\django_vue_exam\django_vue\{image_url_save}'
        # 获取图片文件夹中的所有文件
        image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
        # 确认文件夹中存在图片文件
        if not image_files:
            return JsonResponse({'code':400,'errmsg':'识别错误'})
        # 获取第一张图片的完整路径
        image_path = os.path.join(image_folder, image_files[0])
        # 打开图片文件
        with open(image_path, 'rb') as file:
            image_data = base64.b64encode(file.read()).decode('utf-8')
            response = JsonResponse({'code': 200, 'errmsg': 'ok', 'image': image_data})
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(image_path)
        return response
    def post(self,request):
        print(request)
        file = request.FILES['file']
        print(file.chunks())
        # 处理文件（这里仅简单地将文件保存到 media 目录）
        with open(f'media/detections_image/{file.name}', 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        # 返回处理结果
        return JsonResponse({'status': 'success'})
# 播放本地视频
# 将本地视频以视频流发送给前端
    # def get(self, request):
        # filename = 'media/detections_vedio/2.mp4'
        # filesize = os.path.getsize(filename)
        # def serve_video_chunk():
        #     with open(filename, 'rb') as f:
        #         while True:
        #             chunk = f.read(8192)
        #             if not chunk:
        #                 break
        #             yield chunk
        #
        # response = StreamingHttpResponse(serve_video_chunk(), content_type='video/mp4')
        # response['Content-Length'] = filesize
        # return response
class yoloDetectVedio(View):
    """Django流传输实例：StreamingHttpResponse"""
    def get(self, request):
        filename = 'media/detections_vedio/2.mp4'
        filesize = os.path.getsize(filename)
        def serve_video_chunk():
            with open(filename, 'rb') as f:
                while True:
                    chunk = f.read(8192)
                    if not chunk:
                        break
                    yield chunk

        response = StreamingHttpResponse(serve_video_chunk(), content_type='video/mp4')
        response['Content-Length'] = filesize
        return response

    def post(self,request):
        file = request.FILES.get('file')
        # 处理上传的视频文件，例如保存到指定路径下
        with open('media/detections_image/2023-12-16 14-53-14.mp4', 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # 返回保存后的视频给前端
        video_path = 'media/detections_image/2023-12-16 14-53-14.mp4'
        return FileResponse(open(video_path, 'rb'), content_type='video/mp4')


class openCameraView(View):
    def get(self,request):
        """通过摄像头地址打开摄像头"""
        camera_url = request.GET.get('camera_url')
        print(camera_url)
        try:
            capture = cv2.VideoCapture(f'{camera_url}')
            while capture.isOpened():
                ret,frame = capture.read()


        except:
            return JsonResponse({'code':400,'errmsg':'摄像头打开失败'})
        return JsonResponse({'code':0,'errmsg':'ok'})
























