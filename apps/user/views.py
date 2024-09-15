from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db import connection
from apps.user.tests import send_email
from django_redis import get_redis_connection
import json
# Create your views here.
class showUserName(View):
    def get(self,request):
        username = request.GET.get('registerName')
        cursor = connection.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM userinfo WHERE userName='{username}'")
        count = cursor.fetchone()[0]
        # print(count)
        return JsonResponse({'code':count})
class showUserEmail(View):
    def get(self,request):
        email = request.GET.get("registerEmail")
        # print(email)
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) "
                       "FROM userinfo "
                       f"WHERE userEmail='{email}'")
        count = cursor.fetchone()[0]
        # print(count)
        return JsonResponse({'code':count})
class sendEmail(View):
    def get(self,request):
        email = request.GET.get("registerEmail")
        # print(email)
        content = request.GET.get('content')
        # print(content)
        code =content[15:21]
        # print(code)
        # 提取发送短信的标记-查看有没有-----防止用户频繁发送验证码
        # 用redis存储
        redis_cli = get_redis_connection('code')
        send_flag = redis_cli.get(f'register_flag_{email}')
        if send_flag is not None:
            return JsonResponse({'code':1})
        # pipeline操作Redis数据库 解决redis服务端同时处理多个请求加上网络延迟，服务端利用率不高，效率降低。
        # 执# 创建Redis管道
        pl = redis_cli.pipeline()
        pl.setex('register_%s' % email, 300, code)
        pl.setex('register_flag_%s' % email, 60, 1)
        # 执行请求
        pl.execute()
        send_email(email,content)
        return JsonResponse({'code': 0})
class insertRegisterInfo(View):
    def post(self,request):
        # print(request.body)
        json_data = json.loads(request.body)
        # print(json_data)
        username = json_data.get('userName')
        # print(username)
        password = json_data.get('userPass')
        # print(password)
        email = json_data.get('userEmail')
        # print(email)
        code = json_data.get('userCode').encode()
        # print(code)
        redis_cli = get_redis_connection('code')
        redis_code = redis_cli.get(f'register_{email}')
        # print(redis_code)
        if code==redis_code:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO userinfo (userName, userPass, userEmail) VALUES (%s, %s, %s)",
                           (username, password, email))
        else:
            return JsonResponse({'code':1})
        return JsonResponse({'code':0})
class loginShowAllUserInfo(View):
    def get(self,request):
        loginName = request.GET.get('loginName')
        # print(loginName)
        loginPass = request.GET.get('loginPass')
        # print(loginPass)
        cursor = connection.cursor()
        cursor.execute(f"SELECT userPass FROM userinfo WHERE userName='{loginName}'")
        password = cursor.fetchone()
        # print(password)
        if password[0] is not None:
            if password[0]==loginPass:
                cursor = connection.cursor()
                cursor.execute(f"SELECT userId,userName,userEmail,userType,userSignature,userIcon,userPass FROM userinfo WHERE userName='{loginName}'")
                userInfo = cursor.fetchone()
                if userInfo[3]==0:
                    # 表示为管理员
                    cursor.execute("""SELECT 
                                          parent.id AS id,
                                          parent.name AS name,
                                          parent.chineseName AS chineseName,
                                          parent.title AS title,
                                          parent.path AS path,
                                          parent.icon AS icon,
                                          parent.parentMenuId AS parentMenuId,
                                          parent.menuStatus AS menuStatus,
                                          child.id AS childId,
                                          child.name AS childName,
                                          child.chineseName AS childChineseName,
                                          child.title AS childTitle,
                                          child.path AS childPath,
                                          child.icon AS childIcon,
                                          child.parentMenuId AS childParentMenuId,
                                          child.menuStatus AS childMenuStatus
                                        FROM 
                                          backstagemenuinfo AS parent
                                        LEFT JOIN 
                                          backstagemenuinfo AS child ON parent.id = child.parentMenuId
                                        ORDER BY 
                                          parent.id ASC, child.id ASC""")
                    mennui = cursor.fetchall()
                else:
                    cursor.execute("""SELECT 
                                          parent.id AS id,
                                          parent.name AS name,
                                          parent.chineseName AS chineseName,
                                          parent.title AS title,
                                          parent.path AS path,
                                          parent.icon AS icon,
                                          parent.parentMenuId AS parentMenuId,
                                          parent.menuStatus AS menuStatus,
                                          child.id AS childId,
                                          child.name AS childName,
                                          child.chineseName AS childChineseName,
                                          child.title AS childTitle,
                                          child.path AS childPath,
                                          child.icon AS childIcon,
                                          child.parentMenuId AS childParentMenuId,
                                          child.menuStatus AS childMenuStatus
                                        FROM 
                                          backstagemenuinfo AS parent
                                        LEFT JOIN 
                                          backstagemenuinfo AS child ON parent.id = child.parentMenuId
                                        WHERE 
                                          parent.menuStatus = 1
                                        ORDER BY 
                                          parent.id ASC, child.id ASC""")
                    mennui = cursor.fetchall()
                # 定义一个空字典，用于存储所有菜单项
                menu_dict = {}

                # 遍历查询结果中的每一行记录
                for item in mennui:
                    # 将该行记录转换为字典
                    item_dict = {
                        "id": item[0],
                        "name": item[1],
                        "chineseName": item[2],
                        "title": item[3],
                        "path": item[4],
                        "icon": item[5],
                        "parentMenuId": item[6],
                        "menuStatus": item[7],
                        "childMenu": []
                    }

                    # 如果该菜单项没有父级菜单，则将其添加到 menu_dict 中
                    if item_dict["parentMenuId"] == 0:
                        menu_dict[item_dict["id"]] = item_dict
                    # 否则将其作为子菜单项添加到相应的父级菜单项中
                    else:
                        parent_id = item_dict["parentMenuId"]
                        if parent_id in menu_dict:
                            menu_dict[parent_id]["childMenu"].append(item_dict)

                # 将 menu_dict 转换为列表形式，并按照 id 排序
                menu_list = sorted(menu_dict.values(), key=lambda x: x["id"])
                info = {
                    'userId':userInfo[0],
                    'userName':userInfo[1],
                    'userEmail':userInfo[2],
                    'userType':userInfo[3],
                    'userSignature':userInfo[4],
                    'userIcon': userInfo[5],
                    'userPass': userInfo[6],
                    'menuInfo':menu_list
                }
                return JsonResponse({'data':info,'code': 0})
            else:
                return JsonResponse({'code': 1})
        else:
            return JsonResponse({'code': 1})

class insertLoginInfo(View):
    def get(self,request):
        userId = request.GET.get('userId')
        # print(userId)
        cursor = connection.cursor()
        if userId is not None:
            cursor.execute(f"INSERT INTO logininfo (loginId) VALUES ('{userId}')")
        return JsonResponse({'code': 0})
# 找回密码
# 将输入的用户名或邮箱传给后台，判断是否存在该用户
class showUserNameOrEmail(View):
    def get(self,request):
        userNameOrEmail = request.GET.get('userNameOrEmail')
        # print(userNameOrEmail)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM userinfo WHERE userEmail='{userNameOrEmail}'")
        row = cursor.fetchone()
        info={
            'userId':row[0],
            'userType':row[1],
            'userName':row[2],
            'userPass':row[3],
            'userEmail':row[4],
        }
        return JsonResponse({'code': 0,'data':info})
class sendEmailReset(View):
    def get(self,request):
        email = request.GET.get("resetEmail")
        # print(email)
        content = request.GET.get('content')
        # print(content)
        code =request.GET.get('code')
        # print(code)
        # 提取发送短信的标记-查看有没有-----防止用户频繁发送验证码
        # 用redis存储
        redis_cli = get_redis_connection('code')
        send_flag = redis_cli.get(f'resetEmail_flag_{email}')
        if send_flag is not None:
            return JsonResponse({'code':1})
        # pipeline操作Redis数据库 解决redis服务端同时处理多个请求加上网络延迟，服务端利用率不高，效率降低。
        # 执# 创建Redis管道
        pl = redis_cli.pipeline()
        pl.setex('resetEmail_%s' % email, 300, code)
        pl.setex('resetEmail_flag_%s' % email, 60, 1)
        # 执行请求
        pl.execute()
        send_email(email,content)
        return JsonResponse({'code': 0})
class updateUserPass(View):
    def get(self,request):
        userPass = request.GET.get("userPass")
        userEmail = request.GET.get('userEmail')
        try:
            cursor = connection.cursor()
            cursor.execute(f"UPDATE userinfo SET userPass='{userPass}' WHERE userEmail='{userEmail}'")
        except:
            print('重置失败')
            return JsonResponse({'code':1})
        return JsonResponse({'code':0})