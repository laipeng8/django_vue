# yolov8 模型检测

import cv2
from ultralytics import YOLO
# model = YOLO('D:/Django_project/django_vue_exam/django_vue/utils/weights/yolov8s.pt')

class Detect:
    def __init__(self):
        self.model = YOLO('utils/weights/yolov8s.pt')
    def get_image_result(self,image):
        image_list = self.model.predict(source=image, save=True, name='output')
        image_url = image_list[0].save_dir
        return image_url
    def get_video_result(self,video):
        cap = cv2.VideoCapture(video)
        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),)
        # 第一个参数是将检测视频存储的路径
        out = cv2.VideoWriter('video/save.mp4', cv2.VideoWriter_fourcc(*'avc1'), 40, size)

        pass

# a = model.predict(source="https://assets-global.website-files.com/5f6bc60e665f54545a1e52a5/6452899d5b91e2a5af836f9d_demo-fruit.webp",save=True,name='output')
# print(a[0].save_dir)
# runs\detect\output16获取到保存的路径
# image_url = 'https://assets-global.website-files.com/5f6bc60e665f54545a1e52a5/6452899d5b91e2a5af836f9d_demo-fruit.webp'
# detector = Detect()
# a= detector.get_image_result('media/detections_vedio/1.mp4')
# print(11111111111111111111111)
# print(a)
# print(type(a))



import cv2
from django.http import StreamingHttpResponse
from django.views import View
from ultralytics import YOLO

class YoloDetectVideo(View):
    def get(self, request):
        # 加载 YOLOv5 模型
        model = YOLO('D:/Django_project/django_vue_exam/django_vue/utils/weights/yolov8s.pt')

        # 使用本地摄像头或视频文件
        cap = cv2.VideoCapture('media/detections_vedio/2.mp4')

        # 检查摄像头是否成功打开
        if not cap.isOpened():
            return HttpResponse("Error: Could not open camera or video file.")

        # 获取视频的帧率和尺寸
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 设置响应的 Content-Type
        response = StreamingHttpResponse(self.yolo_detect_frames(cap, model), content_type='multipart/x-mixed-replace;boundary=frame')
        response['Content-Length'] = 0  # 设置为0，让浏览器一直等待新的帧

        return response

    def yolo_detect_frames(self, cap, model):
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            # 进行目标检测
            results = model(frame)

            # 在帧上绘制检测结果
            for label, confidence, box in results.xyxy[0]:
                x, y, w, h = map(int, box)

                # 在帧上绘制矩形框和标签
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} ({confidence:.2f})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # 将检测后的帧转换为JPEG格式
            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

        cap.release()



