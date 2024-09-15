from django.shortcuts import render
from django.views import View
# Create your views here.
from django.db import connection
from django.http import JsonResponse
import os
import json
from apps.front.data_handle import time_handle
from datetime import datetime
from django.http import QueryDict
# 后台
class Cursor:
    """
    数据库查询器
    """
    def Fetchone(self,sql):
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor.fetchone()
    def Fethall(self,sql):
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
class showAllClassifyInfo(View,Cursor):
    def get(self,request):
        # 查询文章分类
        # 执行原始的 SQL 查询
        sql = f"SELECT * from classifyinfo"
        rows = self.Fethall(sql)
        data=[]
        for row in rows:
            info={
                'classifyIntroduce': row[0],
                'classifyId': row[1],
                'classifyName':row[2],
                'articleNumber':row[3],
                'color1':row[4],
                'color2':row[5],
            }
            data.append(info)
        return JsonResponse({'data':data})
class showUserCount(View,Cursor):
    def get(self,request):
        sql = f"SELECT COUNT(*) FROM userinfo"
        userCount = self.Fetchone(sql)
        return JsonResponse({'count': userCount})
class showArticleCount(View,Cursor):
    def get(self,request):
        sql = f"SELECT COUNT(*) FROM articleinfo"
        articleCount = self.Fetchone(sql)
        # print('qqqqqqqqqqqqqqqq')
        # print(articleCount)
        return JsonResponse({'count':articleCount})
class CommentCount(View,Cursor):
    def get(self,request):
        sql = f"SELECT COUNT(*) FROM commentinfo"
        commentCount = self.Fetchone(sql)
        return JsonResponse({'count':commentCount})

class thumbnailUpload(View):
    def post(self, request):
        file = request.FILES.get('file')  # 获取上传的文件对象
        file_path = os.path.join('dist', 'thumbnail', file.name)  # 拼接文件保存路径
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # 如果文件夹不存在，就创建文件夹
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)  # 保存文件

        return JsonResponse({'status': 'success', 'path': file_path})
# 文章操作-新建文章
class insertArticleInfo(View,Cursor):
    def post(self,request):
        json_data = json.loads(request.body)
        userId = json_data.get('userId')
        userName = json_data.get('userName')
        articleTitle = json_data.get('articleTitle')
        articleTitle = articleTitle.replace("'", '"')
        articleClassifyId = json_data.get('articleClassifyId')
        articleClassifyName = json_data.get('articleClassifyName')
        articleDase = json_data.get('articleDase')
        articleDase = articleDase.replace("'", '"')
        articleImgLitimg = json_data.get('articleImgLitimg')
        Content = json_data.get('articleContent')
        # print(articleContent)
        # 将字符串中的 ' 替换为 ^
        articleContent =Content.replace("'", '"')
        articleState = json_data.get('articleState')
        articlePass = json_data.get('articlePass')
        commentState = json_data.get('commentState')
        sql = f"INSERT INTO articleinfo (userId, userName, articleTitle, articleClassifyId, articleClassifyName, articleDase, articleImgLitimg, articleContent, articleState, articlePass, commentState) VALUES ('{userId}', '{userName}', '{articleTitle}','{articleClassifyId}', '{articleClassifyName}', '{articleDase}', '{articleImgLitimg}', '{articleContent}', '{articleState}', '{articlePass}', '{commentState}')"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})

class updateArticleNumberByClassifyId(View,Cursor):
    def get(self,request):
        classifyId = request.GET.get('classifyId')
        sql = f"UPDATE classifyinfo SET articleNumber=articleNumber+1 WHERE classifyId={classifyId}"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})

#文章操作- 文章管理
class articleManage(View,Cursor):
    def get(self,request):
        currentPage = request.GET.get('currentPage')
        start_index = (int(currentPage) - 1) * 5
        pageSize = request.GET.get('pageSize')
        userType = int(request.GET.get('userType'))
        userId = request.GET.get('userId')
        sql_0 = f"SELECT * FROM articleinfo LIMIT {start_index},{pageSize}"
        sql_1 = f"SELECT * FROM articleinfo WHERE userId={userId} LIMIT {start_index},{pageSize}"
        sql_count_0 =f"SELECT COUNT(*) FROM articleinfo"
        sql_count_1 = f"SELECT COUNT(*) FROM articleinfo WHERE userId={userId}"
        if userType==0:
            # print('管理员')
            rows = self.Fethall(sql_0)
            count = self.Fetchone(sql_count_0)
        else:
            rows = self.Fethall(sql_1)
            count = self.Fetchone(sql_count_1)
        articleInfo = []
        for row in rows:
            publishTime_str=row[9].strftime("%Y-%m-%d") if isinstance(row[9], datetime) else row[9]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[3],
                "userName": row[2],
                "articleImgLitimg": row[7].decode('utf-8') if isinstance(row[7], bytes) else row[7],
                "articleDase": row[6],
                "publishTime":timestamp ,
                "articleClassifyName": row[5],
                'articleState':row[10],
                'articlePass':row[11],
                'commentState': row[12],
                "click": row[13],
                "review": row[14],
            }
            articleInfo.append(info)
        # print(count[0])
        data = {'list': articleInfo, 'total': count[0], 'pageSize': pageSize, 'currentPage': currentPage}

        return JsonResponse({'data': data, 'articleCount': count[0]})

# 加载搜索数据
class articleSearchTitle(View,Cursor):
    def get(self,request):
        currentPage = request.GET.get('currentPage')
        start_index = (int(currentPage) - 1) * 5
        pageSize = request.GET.get('pageSize')
        userType = int(request.GET.get('userType'))
        userId = request.GET.get('userId')
        articleTitle = request.GET.get('articleTitle')
        # print(articleTitle)
        sql_0_search = f"SELECT * FROM articleinfo WHERE articleTitle LIKE '%{articleTitle}%' LIMIT {start_index},{pageSize}"
        sql_0_search_count = f"SELECT COUNT(*) FROM articleinfo WHERE articleTitle LIKE '%{articleTitle}%'"
        sql_1_search = f"SELECT * FROM articleinfo WHERE userId={userId} AND articleTitle LIKE '%{articleTitle}%' LIMIT {start_index},{pageSize}"
        sql_1_search_count = f"SELECT COUNT(*) FROM articleinfo WHERE articleTitle LIKE '%{articleTitle}%' AND userId={userId}"
        if userType ==0:
            rows = self.Fethall(sql_0_search)
            count = self.Fetchone(sql_0_search_count)
        else:
            rows = self.Fethall(sql_1_search)
            count = self.Fetchone(sql_1_search_count)
        # print(rows)
        articleInfo = []
        for row in rows:
            publishTime_str = row[9].strftime("%Y-%m-%d") if isinstance(row[9], datetime) else row[9]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[3],
                "userName": row[2],
                "articleImgLitimg": row[7].decode('utf-8') if isinstance(row[7], bytes) else row[7],
                "articleDase": row[6],
                "publishTime": timestamp,
                "articleClassifyName": row[5],
                'articleState': row[10],
                'articlePass': row[11],
                'commentState': row[12],
                "click": row[13],
                "review": row[14],
            }
            articleInfo.append(info)
        # print(count[0])
        # print(articleInfo)
        data = {'list': articleInfo, 'total': count[0], 'pageSize': pageSize, 'currentPage': currentPage}

        return JsonResponse({'data': data, 'articleCount': count[0]})

class articleSearchPass(View,Cursor):
    def get(self,request):
        currentPage = request.GET.get('currentPage')
        start_index = (int(currentPage) - 1) * 5
        pageSize = request.GET.get('pageSize')
        userType = int(request.GET.get('userType'))
        userId = request.GET.get('userId')
        articlePass = request.GET.get('articlePass')
        sql_0_pass = f"SELECT * FROM articleinfo  WHERE articlePass={articlePass} LIMIT {start_index},{pageSize}"
        sql_0_pass_count = f"SELECT COUNT(*) FROM articleinfo WHERE articlePass={articlePass}"
        sql_1_pass = f"SELECT * FROM articleinfo WHERE userId={userId} AND articlePass={articlePass} LIMIT {start_index},{pageSize}"
        sql_1_pass_count = f"SELECT COUNT(*) FROM articleinfo WHERE articlePass={articlePass} AND userId={userId}"
        if userType ==0:
            rows = self.Fethall(sql_0_pass)
            count = self.Fetchone(sql_0_pass_count)
        else:
            rows = self.Fethall(sql_1_pass)
            count = self.Fetchone(sql_1_pass_count)
        # print(rows)

        articleInfo = []
        for row in rows:
            publishTime_str = row[9].strftime("%Y-%m-%d") if isinstance(row[9], datetime) else row[9]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[3],
                "userName": row[2],
                "articleImgLitimg": row[7].decode('utf-8') if isinstance(row[7], bytes) else row[7],
                "articleDase": row[6],
                "publishTime": timestamp,
                "articleClassifyName": row[5],
                'articleState': row[10],
                'articlePass': row[11],
                'commentState': row[12],
                "click": row[13],
                "review": row[14],
            }
            articleInfo.append(info)
        # print(count[0])

        data = {'list': articleInfo, 'total': count[0], 'pageSize': pageSize, 'currentPage': currentPage}

        return JsonResponse({'data': data, 'articleCount': count[0]})
# 文章操作-分类管理
class classifyManager(View,Cursor):
    def post(self,request):
        json_data = json.loads(request.body)
        classifyName = json_data.get('classifyName')
        color1 = json_data.get('color1')
        color2 = json_data.get('color2')
        classifyIntroduce = json_data.get('classifyIntroduce')
        sql = f"INSERT INTO classifyinfo(classifyIntroduce,classifyName,color1,color2) VALUES ('{classifyIntroduce}','{classifyName}','{color1}','{color2}')"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})
    def delete(self,request):
        classifyId = request.GET.get('classifyId')
        sql = f"DELETE FROM classifyinfo WHERE classifyId={classifyId}"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})

# 评论管理
class commentManager(View,Cursor):
    def get(self,request):
        currentPage = request.GET.get('currentPage')
        start_index = (int(currentPage) - 1) * 5
        pageSize = request.GET.get('pageSize')
        userType = int(request.GET.get('userType'))
        userId = request.GET.get('userId')
        searchContent =request.GET.get('searchContent')
        # print(searchContent)
        sql_0 = (f"SELECT ci.commentId, ci.articleId, ci.userId, ci.content, ci.parentId, ci.commentDate, ai.articleTitle, u.userName "
                 f"FROM commentinfo ci "
                 f"LEFT JOIN articleinfo ai ON ci.articleId = ai.articleId "
                 f"LEFT JOIN userinfo u ON ci.userId = u.userId "
                 f"LIMIT {start_index},{pageSize}")
        sql_0_search=(f"SELECT ci.commentId, ci.articleId, ci.userId, ci.content, ci.parentId, ci.commentDate, ai.articleTitle, u.userName "
                      f"FROM commentinfo ci "
                      f"LEFT JOIN articleinfo ai ON ci.articleId = ai.articleId "
                      f"LEFT JOIN userinfo u ON ci.userId = u.userId "
                      f"WHERE ci.content LIKE '%{searchContent}%'")
        sql_1 = (f"SELECT ci.commentId, ci.articleId, ci.userId, ci.content, ci.parentId, ci.commentDate, ai.articleTitle, u.userName "
                 f"FROM commentinfo ci "
                 f"LEFT JOIN articleinfo ai ON ci.articleId = ai.articleId "
                 f"LEFT JOIN userinfo u ON ci.userId = u.userId "
                 f"WHERE ci.userId = {userId}")
        sql_1_search = (f"SELECT ci.commentId, ci.articleId, ci.userId, ci.content, ci.parentId, ci.commentDate, ai.articleTitle, u.userName "
                        f"FROM commentinfo ci "
                        f"LEFT JOIN articleinfo ai ON ci.articleId = ai.articleId "
                        f"LEFT JOIN userinfo u ON ci.userId = u.userId "
                        f"WHERE ci.userId = {userId} AND ci.content LIKE '%{searchContent}%'")
        if userType==0:
            if searchContent is None:
                rows = self.Fethall(sql_0)
            else:
                rows = self.Fethall(sql_0_search)
        else:
            if searchContent is None:
                rows = self.Fethall(sql_1)
            else:
                rows = self.Fethall(sql_1_search)
        articleInfo = []
        for row in rows:
            # publishTime_str = row[5].strftime("%Y-%m-%d") if isinstance(row[5], datetime) else row[5]
            # timestamp = time_handle(publishTime_str)
            info = {
                "commentId": row[0],
                "articleId": row[1],
                "userId": row[2],
                "content": row[3],
                "parentId": row[4],
                "commentDate": row[5],
                'articleTitle':row[6],
                'userName': row[7],
            }
            articleInfo.append(info)
        sql_0_count = f"SELECT COUNT(*) FROM commentinfo"
        count = self.Fetchone(sql_0_count)[0]
        # print(count)

        data = {'list': articleInfo, 'total': count, 'pageSize': pageSize, 'currentPage': currentPage}

        return JsonResponse({'data': data, 'articleCount': count})

    def delete(self, request):
        # 获取传递的参数
        comment_id = request.GET.get("commentId")
        sql =f"DELETE FROM commentinfo WHERE commentId={comment_id}"
        self.Fetchone(sql)
        return JsonResponse({'code':0})
# 用户管理
class userManager(View,Cursor):
    def get(self,request):
        currentPage = request.GET.get('currentPage')
        start_index = (int(currentPage) - 1) * 5
        pageSize = request.GET.get('pageSize')
        searchContent = request.GET.get('searchContent')
        if searchContent is None:
            searchContent=''
        # sql1 = f"SELECT * FROM userinfo LIMIT {start_index},{pageSize}"
        sql2 = f"SELECT * FROM userinfo WHERE userName LIKE '%{searchContent}%' LIMIT {start_index},{pageSize}"
        rows = self.Fethall(sql2)
        userList = []
        for row in rows:
            publishTime_str=row[5].strftime("%Y-%m-%d") if isinstance(row[5], datetime) else row[5]
            timestamp = time_handle(publishTime_str)
            info={
                'userName':row[2],
                'userEmail':row[4],
                'userType':row[1],
                'userIcon':row[-1],
                'userSignature':row[-2],
                'userRegdate':timestamp
            }
            userList.append(info)
        data = {'list': userList, 'total': len(userList), 'pageSize': pageSize, 'currentPage': currentPage}
        return JsonResponse({'data':data})
    def post(self,request):
        json_data = json.loads(request.body)
        userId = json_data.get('userId')
        userName = json_data.get('userName')
        userPass = json_data.get('userPass')
        userEmail = json_data.get('userEmail')
        userSignature = json_data.get('userSignature')
        userType = json_data.get('userType')
        sql = f"UPDATE userinfo SET userName='{userName}' AND userPass='{userPass}' AND userEmail='{userEmail}' AND userSignature='{userSignature}' AND userType='{userType}' WHERE userId = '{userId}'"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})
    def delete(self,request):
        userId = request.GET.get('userId')
        sql = f"DELETE FROM userinfo WHERE userId={userId}"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})
# 链接管理
class linkManage(View,Cursor):
    def get(self,request):
        currentPage = request.GET.get('currentPage')
        start_index = (int(currentPage) - 1) * 5
        pageSize = request.GET.get('pageSize')
        searchContent = request.GET.get('searchContent')
        if searchContent is None:
            searchContent=''
        sql = f"SELECT * FROM urlinfo WHERE urlName LIKE '%{searchContent}%' LIMIT {start_index},{pageSize}"
        rows = self.Fethall(sql)
        userList = []
        for row in rows:
            info={
                'urlId':row[0],
                'urlName':row[1],
                'urlAddres':row[2],
                'urlReferral':row[3],
                'urlLitimg': row[4],
                'webmasterEmail':row[5],
                'urlPass':row[6],
                'urlType': row[7],
            }
            userList.append(info)
        # print(userList)
        data = {'list': userList, 'total': len(userList), 'pageSize': pageSize, 'currentPage': currentPage}
        return JsonResponse({'data':data})
    def delete(self,request):
        urlId = request.GET.get('urlId')
        sql = f"DELETE FROM urlinfo WHERE urlId={urlId}"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})
# 链接管理-添加链接
class auditScreening(View,Cursor):
    def get(self,request):
        currentPage = request.GET.get('currentPage')
        pageSize = request.GET.get('pageSize')
        auditContent = request.GET.get('auditContent')
        if auditContent is None:
            auditContent=''
        sql = f"SELECT * FROM urlinfo WHERE urlPass={auditContent} LIMIT {start_index},{pageSize}"
        rows = self.Fethall(sql)
        userList = []
        for row in rows:
            info={
                'urlId':row[0],
                'urlName':row[1],
                'urlAddres':row[2],
                'urlReferral':row[3],
                'webmasterEmail':row[4],
                'urlPass':row[5],
                'urlType': row[6],
            }
            userList.append(info)
        data = {'list': userList, 'total': len(userList), 'pageSize': pageSize, 'currentPage': currentPage}
        return JsonResponse({'data':data})
class updateUrlPass(View,Cursor):
    def get(self,request):
        urlId = request.GET.get('urlId')
        urlPass = request.GET.get('urlPass')
        sql = f"UPDATE urlinfo SET urlPass={urlPass} WHERE urlId={urlId}"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})
class updateUserBasicsInfo(View,Cursor):
    def get(self,request):
        userId =request.GET.get('userId')
        userName = request.GET.get('userName')
        userSignature = request.GET.get('userSignature')
        userIcon = request.GET.get('userIcon')
        sql = (f"UPDATE userinfo "
               f"SET userName = '{userName}', userSignature = '{userSignature}', userIcon = '{userIcon}' "
               f"WHERE userId = {userId}")
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})
class updateUserEmail(View,Cursor):
    def get(self,request):
        userId = request.GET.get('userId')
        userEmail = request.GET.get('userEmail')
        sql = f"UPDATE userinfo SET userEmail='{userEmail}' WHERE userId = '{userId}'"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})
class updateUserPass(View,Cursor):
    def get(self,request):
        userId = request.GET.get('userId')
        userPass = request.GET.get('userPass')
        sql = f"UPDATE userinfo SET userPass='{userPass}' WHERE userId = '{userId}'"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})

# 系统设置
class updateSystemSetup(View,Cursor):
    def post(self,request):
        json_data = json.loads(request.body)
        stickArticle = json_data.get('stickArticle')
        allArticle = json_data.get('allArticle')
        featuredArticle = json_data.get('featuredArticle')
        technologyArticle = json_data.get('technologyArticle')
        resourceArticle = json_data.get('resourceArticle')
        advertising1 = json_data.get('advertising1')
        advertisingLink1 = json_data.get('advertisingLink1')
        advertising2 = json_data.get('advertising2')
        advertisingLink2 = json_data.get('advertisingLink2')
        advertising3 = json_data.get('advertising3')
        advertisingLink3 = json_data.get('advertisingLink3')
        effects01 = json_data.get('effects01')
        effects02 = json_data.get('effects02')
        sql = f"UPDATE systemsetup SET stickArticle='{stickArticle}',allArticle='{allArticle}',featuredArticle='{featuredArticle}',technologyArticle='{technologyArticle}',resourceArticle='{resourceArticle}',advertising1='{advertising1}',advertisingLink1='{advertisingLink1}',advertising2='{advertising2}',advertisingLink2='{advertisingLink2}',advertising3='{advertising3}',advertisingLink3='{advertisingLink3}',effects01={effects01},effects02={effects02}"
        try:
            self.Fetchone(sql)
            return JsonResponse({'code':0})
        except:
            return JsonResponse({'code':1})
