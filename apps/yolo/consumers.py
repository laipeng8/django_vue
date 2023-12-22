from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from ultralytics import YOLO
import base64
import cv2

class Detector:
    def __init__(self):
        super().__init__()
        self.model = YOLO('utils/weights/yolov8s.pt')
    def get_file_capture(self,video_file):
        return cv2.VideoCapture(video_file)
    def get_text_capture(self):
        video_path = r"D:\Django_project\django_vue_exam\django_vue\media\detections_vedio\2.mp4"
        return cv2.VideoCapture(video_path)
    def get_camera_capture(self):
        # 获取摄像头捕获对象或视频文件捕获对象
        return cv2.VideoCapture(0)
    def get_frame_data(self, frame,conf, results):
        # 绘制预测结果，并返回 JPEG 格式的 base64 编码的帧数据
        for result in results:
            # 绘制矩形框
            for box in result.boxes:
                xyxy = box.xyxy.squeeze().tolist()
                x1, y1, x2, y2 = int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                c, conf, id = int(box.cls), float(box.conf) if conf else None, None if box.id is None else int(
                    box.id.item())
                name = ('' if id is None else f'id:{id} ') + result.names[c]
                label = name
                confidence = conf
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0),
                            2)
        ret, buffer = cv2.imencode('.jpg',frame)
        frame_base64 = base64.b64encode(buffer).decode('utf-8')
        return frame_base64

class VideoConsumer(WebsocketConsumer):
    def __init__(self):
        self.model = YOLO('utils/weights/yolov8s.pt')
    def websocket_connect(self, message):
        self.accept()
        # （前端发送websocket请求，自动触发）
        # 接收客户端连接
        # 得到cap
        detector = Detector()
        cap = detector.get_text_capture()
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break
            results = self.model(frame, False, conf=0.8)
            conf = True
            # 绘制预测结果
            frame_base64 = detector.get_frame_data(frame,conf,results)
            # 发送视频帧给前端
            self.send(text_data=frame_base64)
            self.channel_layer.group_send(
                "video_group",
                {
                    "type": "send_video_frame",
                    "frame_base64": frame_base64,
                }
            )
        cap.release()
        self.close()
    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发
        print(message)
        # self.send(message['text'])
        # 服务端主动断开
        # self.close()
    def websocket_disconnect(self, message):
        # 断开连接  （前端与服务端断开连接自动触发）
        cap.release()
        raise StopConsumer()

class VideoFileConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        print('请求连接')
        self.accept()
    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发
        # text = message['text']

        if text=='关闭':
            self.close()
    def websocket_disconnect(self, message):
        # 断开连接  （前端与服务端断开连接自动触发）
        print('断开连接')
        raise StopConsumer()

class VideoCameraConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        print('请求连接')
        self.accept()
    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发
        # text = message['text']

        if text=='关闭':
            self.close()
    def websocket_disconnect(self, message):
        # 断开连接  （前端与服务端断开连接自动触发）
        print('断开连接')
        raise StopConsumer()