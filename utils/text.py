# from ultralytics import YOLO
#
# # Load a model
# model = YOLO('utils/weights/yolov8s.pt')  # pretrained YOLOv8n model
#
# # 对图像列表运行批处理推理
# results = model(['media/detections_vedio/2.mp4'], stream=True)  # 返回 Results 对象的生成器
#
# # 过程结果生成器
# for result in results:
#     boxes = result.boxes  # bbox 输出的 boxes 对象
#     masks = result.masks  # 用于分割掩码输出的掩码对象
#     keypoints = result.keypoints  # 姿势输出的关键点对象
#     probs = result.probs  # 分类输出的 Probs 对象



# import os
# import json
# import asyncio
# # from channels.generic.http import AsyncHttpConsumer
# from django.http import HttpResponse
# from ultralytics import YOLO
# video_path = r'D:\Django_project\django_vue_exam\django_vue\media\detections_vedio\2.mp4'
# model = YOLO('utils/weights/yolov8s.pt')
# result = model.predict(source=video_path,show=True)


import cv2
from ultralytics import YOLO

# # Load the YOLOv8 model
# model = YOLO('utils/weights/yolov8s.pt')
#
# # Open the video file
# video_path = r"D:\Django_project\django_vue_exam\django_vue\media\detections_vedio\2.mp4"
# cap = cv2.VideoCapture(video_path)
#
# # 逐帧进行预测
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # 对每一帧进行预测。并设置置信度阈值为0.8，需要其他参数，可直接在后面加
#     results = model(frame, False, conf=0.8)
#     conf = True
#     # 绘制预测结果
#     for result in results:
#         # 绘制矩形框
#         for box in result.boxes:
#             xyxy = box.xyxy.squeeze().tolist()
#             x1, y1, x2, y2 = int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             c, conf, id = int(box.cls), float(box.conf) if conf else None, None if box.id is None else int(
#                 box.id.item())
#             name = ('' if id is None else f'id:{id} ') + result.names[c]
#             label = name
#             confidence = conf
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
#                         2)
#     # 或者使用下行代码绘制所有结果
#     # res=results[0].plot(conf=False)
#     # 显示预测结果
#     cv2.imshow("Predictions", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

class VideoConsumer(WebsocketConsumer):
    def __init__(self):
        self.model = YOLO('utils/weights/yolov8s.pt')
    def websocket_connect(self, message):
        self.accept()
        # （前端发送websocket请求，自动触发）
        # 接收客户端连接
        # 得到cap
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break
            results = self.model(frame, False, conf=0.8)
            conf = True
            # 绘制预测结果
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
            # 将视频帧转换为 JPEG 格式的 base64 编码
            ret, buffer = cv2.imencode('.jpg',frame)
            frame_base64 = base64.b64encode(buffer).decode('utf-8')
            # 发送视频帧给前端
            self.send(text_data=frame_base64)
            self.channel_layer.group_send(
                "video_group",
                {
                    "type": "send_video_frame",
                    "frame_base64": frame_base64,
                }
            )
            # 适当的延时
            # self.delay(0.05)
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






