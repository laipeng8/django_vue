# !/user/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
import time

# 将日期字符串转换成 datetime 对象
publish_time_str = '2022-11-03'
publish_time = datetime.strptime(publish_time_str, '%Y-%m-%d')

# 将 datetime 对象转换成时间戳（毫秒数）
timestamp = int(time.mktime(publish_time.timetuple()) * 1000)
print(timestamp)
# 发送数据时使用 timestamp 替换 publish_time
data = [{'articleId': 61, 'articleTitle': '测试文章1测试文章1测试文章1测试文章1测试文章1', 'articleImgLitimg': '', 'articleClassifyName': '技术', 'publishTime': timestamp}]
def time_handle(time_str):
    publish_time = datetime.strptime(time_str, '%Y-%m-%d')

    # 将 datetime 对象转换成时间戳（毫秒数）
    timestamp = int(time.mktime(publish_time.timetuple()) * 1000)
    return timestamp