import re

import redis
import requests
from django.shortcuts import render
from django.contrib.auth import login
# Create your views here.
from django.views import View
from users.models import User
from django.http import JsonResponse
import json
from libs.yuntongxun.sms import CCP
from django import http
import random
import logging
logger = logging.getLogger('django')
from django_redis import get_redis_connection
class UsernameCountView(View):
    def get(self, request):
        """
        根据用户名查询数据库，判断用户名是否重复
        """
        username = request.GET.get('username')
        count = User.objects.filter(username=username).count()
        return JsonResponse({'code': 0, 'errmsg': 'ok', 'count': count})

class MobileCountView(View):
    def get(self, request):
        """
        根据手机号查询数据库，判断手机号是否存在
        """
        mobile_num = request.GET.get('mobile')
        count = User.objects.filter(mobile=mobile_num).count()
        #print('电话号码' + str(count))
        return JsonResponse({'code': 0, 'errmsg': 'ok', 'count': count})
class RegisterView(View):
    def post(self,request):
        """
        注册
            表单  JSON数据 request.body
            username: '',
            password: '',
            code_id: '',
            remember: false,
            mobile_number: '',
        """
        try:
            json_data = json.loads(request.body)
            username = json_data.get('username')
            password = json_data.get('password')
            mobile_number = json_data.get('mobile_number')
            code_id = json_data.get('code_id')
            remember = json_data.get('remember')
            if not all([username,password,mobile_number,code_id,remember]):
                return JsonResponse({'code':400,'errmsg':'缺少必穿参数'})
            if not re.match( r'^\w{7,16}$',username):
                return JsonResponse({'code': 400, 'errmsg': 'username格式有错'})
            if not re.match( r'^\w{7,16}$',password):
                return JsonResponse({'code': 400, 'errmsg': 'password格式有错'})
            if not re.match(r'^\d{11}$',mobile_number):
                return JsonResponse({'code': 400, 'errmsg': '电话号码格式有错'})
            redis_cli = get_redis_connection('code')
            redis_code = redis_cli.get(f'register_{mobile_number}')
            # 获取的redis_code的类型是<class 'bytes'>  ，所以需要将code_id转换进行比较
            code_id_bytes = code_id.encode()
            if code_id_bytes!=redis_code:
                return JsonResponse({'code': 400, 'errmsg': '验证码有错'})
            try:
                user = User.objects.create_user(username = username,
                                                password = password,
                                                mobile = mobile_number)
            except:
                return JsonResponse({'message': '注册失败','code':400})
            # 状态保持
            # 设置session信息
            request.session['user_id'] = user.id
            print(f'  user.id  = = {user.id}')
            login(request,user)
            return JsonResponse({'message': '注册成功','code':0})
        except json.JSONDecodeError as e:
            # JSON解析错误
            return JsonResponse({'error': 'Invalid JSON format','code':400})

class SMSCodeView(View):
    def get(self,request):
        mobile = request.GET.get('mobile')
        # 连接redis

        redis_cli = get_redis_connection('code')
        # 提取发送短信的标记-查看有没有-----防止用户频繁发送验证码
        send_flag = redis_cli.get(f'register_flag_{mobile}')
        if send_flag is not None:
            return JsonResponse({'code':401,'errmsg':'不要频繁发送短信'})
        # 4生成短信验证码
        from random import randint
        sms_code = "%04d"%randint(0,9999)
        print(sms_code)
        # # 5保存短信验证码---5分钟-300秒
        # redis_cli.setex(mobile,300,sms_code)
        # # 添加一个标记位，防止用户频繁发送验证码 有效期60秒，内容为1-随便什么都可以
        # redis_cli.setex(f'send_flag_{mobile}',60,1)

        # pipeline操作Redis数据库 解决redis服务端同时处理多个请求加上网络延迟，服务端利用率不高，效率降低。
        # 实现步骤
        # 1.
        # 创建Redis管道
        # 2.
        # 将Redis请求添加到队列
        # 3.
        # 执# 创建Redis管道
        pl = redis_cli.pipeline()
        # # 将Redis请求添加到队列
        pl.setex('register_%s' % mobile, 300, sms_code)
        pl.setex('register_flag_%s' % mobile, 60, 1)
        # 执行请求
        pl.execute()     #将上面两次添加redis数据，放在一起执行，减少对redis访问压力
        # # 6发送短信验证码
        # from libs.yuntongxun.sms import CCP
        # CCP().send_template_sms(mobile,[sms_code,5],1)
        from celery_tasks.sms.tasks import celery_send_sms_code
        # deley 的参数 等同于 任务（函数）的参数   delay()是Celery异步任务中的一个方法，用于将任务推送到消息队列中等待执行
        celery_send_sms_code.delay(mobile,sms_code)
        # 状态保持

        return JsonResponse({'code':0,'errmsg':'ok'})


class LoginView(View):
    def post(self,request):
        json_data = json.loads(request.body)
        print(json_data)
        username = json_data.get('username')
        password = json_data.get('password')
        # 可以直接查询数据库
        # 也可以用自带登录方法
        from django.contrib.auth import authenticate
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return JsonResponse({'code':400,'errmsg':"账号密码错误"})
        else:

            # 4状态保持 ----session
            from django.contrib.auth import login
            login(request,user)
            print(1111111111111)
            # 5判断是否记住登陆--在一定时间内免登陆 -默认两周
            # request.session.set_expiry(864000)
            #浏览器关闭就删除
            request.session.set_expiry(0)

            response = JsonResponse({'code': 0, 'errmsg': 'ok'})
            response.set_cookie('username',user.username)
            print(2222222222222)
            print(type(user.username))

        return response


class LoginCodeView(View):
    def get(self,request):
        """发送验证码"""
        mobile = request.GET.get('mobile')
        # 连接redis
        redis_cli = get_redis_connection('code')
        # 提取发短信的标记-防止用户频繁发送短信
        send_flag = redis_cli.get(f'login_flag_{mobile}')
        if send_flag:
            return JsonResponse({})
        # 生成短信验证码
        from random import randint
        sms_code = "%4d"%randint(0,9999)
        print(sms_code)
        # # 保存短信验证码 5分钟后失效  300秒
        #         # redis_cli.setex(mobile,300,sms_code)
        #         # # 添加一个标记位 ，防止用户频繁发送短信 有效期60秒 内容为：1  -随便上面都可以
        #         # redis_cli.setex(f'send_flag_{mobile}',60,1)
        """
        为了缓解redis压力，
        pipeline操作Redis数据库 解决redis服务端同时处理多个请求加上网络延迟，服务端利用率不高，效率降低。
        实现步骤
        1.
        创建Redis管道
        2.
        将Redis请求添加到队列
        3.
        创建Redis管道
        """
        p1 = redis_cli.pipeline()
        # 将redis请求添加到队列
        p1.setex(f'login_{mobile}',300,sms_code)
        p1.setex(f'login_flag_{mobile}',60,1)
        # 执行p1所有任务
        p1.execute() #将上面两次添加redis数据，放在一起执行，减少对redis访问压力
        from celery_tasks.sms.tasks import celery_send_sms_code
        # deley 的参数 等同于 任务（函数）的参数   delay()是Celery异步任务中的一个方法，用于将任务推送到消息队列中等待执行
        celery_send_sms_code.delay(mobile, sms_code)

        return JsonResponse({})#不需要返回响应
    def post(self, request):
        json_data = json.loads(request.body)
        mobile = json_data.get('mobile')
        print(f'mobile:{mobile}')
        code = json_data.get('code')
        print(f'code:{code}')
        # 获取的redis_code的类型是<class 'bytes'>  ，所以需要将code_id转换进行比较
        code_id = code.encode()
        print(f'code_id:{code_id}')
        redis_cli = get_redis_connection('code')
        sms_code = redis_cli.get(f'login_{mobile}')
        print(f'sms_code:{sms_code}')
        user = User.objects.filter(mobile=mobile)
        print(user)
        if code_id==sms_code:
            # 查询数据库  --通过电话号码
            user = User.objects.filter(mobile=mobile)
            print(user)
            # user  查到的是用户名
            # print(user)
            return JsonResponse({'code': 0, 'errmsg': 'ok'})
        else:
            return JsonResponse({'message': '登录失败'}, status=400)

        # # 状态保持
        # from django.contrib.auth import login
        # login(request,user)
# 系统自带退出方法
from django.contrib.auth import logout
class LogoutView(View):
    """
    退出登录
    """
    def delete(self,request):
        print(request)
        logout(request)
        response = JsonResponse({'code':0,'errmsg':'ok'})
        response.delete_cookie('username')
        return response
class translator(View):
    def post(self,request):
        print(request)
        json_data = json.loads(request.body)
        print(json_data)
        # from_lang = json_data.get('from_lang')
        # to_lang = json_data.get('t0_lang')
        # from_lang = 'EN-US'
        to_lang = 'ZH'
        in_str = json_data.get('in_str')
        if len(in_str)<500:
            in_str = in_str[:499]
        translationed = Get_translation().get_str(to_lang,in_str)
        print(translationed)
        return JsonResponse({'code':0,'errmsg':'ok','translated':f'{translationed}'})
from translate import Translator
class Get_translation:
    def get_str(self,to_lang,in_str):
        translator = Translator(to_lang=to_lang)
        translation = translator.translate(f'{in_str}')
        return translation
class Translate(Get_translation):
    """函数重载，根据不同参数，调用不同方法"""
    def china_english(self,to_lang,in_str):
        translator = Translator(to_lang=to_lang)
        translation = translator.translate(f'{in_str}')
        return translation
    def english_china(self,in_translation,to_translation,class_translation):
        pass


