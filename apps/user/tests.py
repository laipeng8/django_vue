from django.test import TestCase

# Create your tests here.
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import smtplib
import time
from email.mime.text import MIMEText


def send_email(send_email,content):
    sender = user = '2195143506@qq.com'  # 发送方的邮箱账号
    passwd = 'surxtpwelzineaff'  # 授权码

    receiver = f'{send_email}'  # 接收方的邮箱账号，不一定是QQ邮箱

    # 纯文本内容
    msg = MIMEText(f'{content}', 'plain', 'utf-8')

    # From 的内容是有要求的，前面的abc为自己定义的 nickname，如果是ASCII格式，则可以直接写
    msg['From'] = f'laipeng <prefix@domain>'
    msg['To'] = receiver
    msg['Subject'] = '【赖鹏的个人博客】'  # 点开详情后的标题

    try:
        # 建立 SMTP 、SSL 的连接，连接发送方的邮箱服务器
        smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)

        # 登录发送方的邮箱账号
        smtp.login(user, passwd)

        # 发送邮件 发送方，接收方，发送的内容
        smtp.sendmail(sender, receiver, msg.as_string())

        print('邮件发送成功')

        smtp.quit()
    except Exception as e:
        print(e)
        print('发送邮件失败')
