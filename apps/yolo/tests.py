# from django.test import TestCase
# import os
# import cv2
# from ultralytics import YOLO
# model = YOLO('D:/Django_project/django_vue_exam/django_vue/utils/weights/yolov8s.pt')
# image_url = 'https://assets-global.website-files.com/5f6bc60e665f54545a1e52a5/6452899d5b91e2a5af836f9d_demo-fruit.webp'
# image_list = model.predict(source=image_url, save=True, name='output')
# image_url_save = image_list[0].save_dir
# a = fr'D:\Django_project\django_vue_exam\django_vue\{image_url_save}'
#
# # Create your tests here.
# # image_folder = r'D:\Django_project\django_vue_exam\django_vue\runs\detect\output10'
# image_folder = a
# # 获取图片文件夹中的所有文件
# image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
# # 确认文件夹中存在图片文件
# if not image_files:
#     print('路径错误')
# else:
#     print('路径正确')
#
#     # 获取第一张图片的完整路径
#     image_path = os.path.join(image_folder, image_files[0])
#     # 读取图像
#     image = cv2.imread(image_path)
#
#     # 显示图像
#     cv2.imshow('First Image', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# import os
#
path = r'D:\Django_project\django_vue_exam\django_vue\runs\detect'
# command = f'attrib -rd "{path}"'  # 构造命令行指令
# result = os.system(command)  # 执行命令
# os.remove(r'D:\Django_project\django_vue_exam\django_vue\runs\detect')

import shutil
shutil.rmtree(path)


































