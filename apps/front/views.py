import time
import json
import os
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views import View
from django.db import connection
from datetime import datetime
from apps.front.data_handle import  time_handle

from django.http import QueryDict

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

#文章分类 -后台首页饼图
class showClassifyInfoByClassifyId(View):
    def get(self,request):
        # 查询文章分类页面的标题--classifyinfo
        classifyId = request.GET.get('classifyId')
        # print(classifyId)
        cursor = connection.cursor()
        cursor.execute(f'SELECT classifyName, classifyIntroduce, articleNumber '
                       f'from classifyinfo '
                       f'WHERE classifyId={classifyId}')
        rows = cursor.fetchone()
        classifyTitle=list()
        for row in rows:
            classifyTitle.append(row)
        return JsonResponse({'code': 0, 'errmsg': 'ok','class':classifyTitle})
#article/byClassifyId?currentPage=1&pageSize=8&classifyId=1
# 文章分类根据classfiid查询所有的文章
class byClassifyId(View):
    def get(self, request):
        currentPage = request.GET.get('currentPage') # 当前页
        # print(currentPage)
        start_index = (int(currentPage) - 1) * 8
        # print(start_index)
        pageSize = request.GET.get('pageSize') # 数据行数
        # print(pageSize)
        classifyId = request.GET.get('classifyId')
        # print(classifyId)
        cursor = connection.cursor()
        cursor.execute(f'SELECT articleId, articleTitle, articleClassifyId, articleClassifyName, articleDase, articleImgLitimg, userName, publishTime, click '
                       f'FROM articleinfo '
                       f'WHERE articleClassifyId = {classifyId} LIMIT {start_index}, {pageSize}')
        rows = cursor.fetchall()
        articleInfo = []
        for row in rows:
            publishTime_str=row[7].strftime("%Y-%m-%d") if isinstance(row[7], datetime) else row[7]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[1],
                "articleImgLitimg": row[5].decode('utf-8') if isinstance(row[5], bytes) else row[5],
                "articleDase": row[4],
                "userName": row[6],
                "publishTime":timestamp ,
                "articleClassifyName": row[3],
                "click": row[8]
            }
            articleInfo.append(info)
        cursor = connection.cursor()
        cursor.execute(f'SELECT COUNT(*) '
                       f'FROM articleinfo '
                       f'WHERE articleClassifyId = {classifyId}')
        count = cursor.fetchone()
        articleCount = count[0]
        data={'list': articleInfo,'total':articleCount,'pageSize':pageSize,'currentPage':currentPage}

        # print(articleCount)
        return JsonResponse({'data': data,'articleCount':articleCount})

# 首页精选  查询系统设置中的精选文章的id
class showAllFeatured(View):
    def get(self,request):
        cursor = connection.cursor()
        cursor.execute('SELECT featuredArticle '
                       'FROM systemsetup')
        article_id = cursor.fetchone()
        # print(article_id)
        return JsonResponse({'featuredArticle':article_id})
# 首页精选 通过精选id查询精选文章
class showAllFeaturedArticleInfo(View):
    def get(self,request):
        a = request.GET.get('featuredData[]')
        if a==None:
            return JsonResponse({})
        a = tuple(map(int, a.strip('[]').split(',')))
        if len(a)==1:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleClassifyName,publishTime '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN ({a[0]})')
        else:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleClassifyName,publishTime '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN {a}')
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        articleInfo = []
        for row in rows:
            publishTime_str=row[4].strftime("%Y-%m-%d") if isinstance(row[4], datetime) else row[4]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[1],
                "articleImgLitimg": row[2].decode('utf-8') if isinstance(row[2], bytes) else row[2],
                "articleClassifyName": row[3],
                "publishTime": timestamp
            }
            articleInfo.append(info)
        # print(articleInfo)
        return JsonResponse({'articleInfo':list(articleInfo)})
# 首页-技术-查询技术文章所有的id列表
class showAllTechnology(View,Cursor):
    def get(self,request):
        sql = f"SELECT technologyArticle FROM systemsetup"
        article_id = self.Fetchone(sql)
        # print(article_id)
        return JsonResponse({'technologyArticle':article_id})
# 首页-技术 通过技术id列表查询技术文章
class showAllTechnologyArticleInfo(View):
    def get(self,request):
        a = request.GET.get('technologyData[]')
        if a==None:
            return JsonResponse({})
        a = tuple(map(int, a.strip('[]').split(',')))
        if len(a)==1:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleClassifyName,publishTime '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN ({a[0]})')
        else:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleClassifyName,publishTime '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN {a}')
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        articleInfo = []
        for row in rows:
            publishTime_str=row[4].strftime("%Y-%m-%d") if isinstance(row[4], datetime) else row[4]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[1],
                "articleImgLitimg": row[2].decode('utf-8') if isinstance(row[2], bytes) else row[2],
                "articleClassifyName": row[3],
                "publishTime": timestamp
            }
            articleInfo.append(info)
        # print(articleInfo)
        return JsonResponse({'articleInfo':list(articleInfo)})
# 首页-资源-查询系统中的资源id
class showAllResource(View):
    def get(self,request):
        cursor = connection.cursor()
        cursor.execute('SELECT technologyArticle FROM systemsetup')
        article_id = cursor.fetchone()
        # print(article_id)
        return JsonResponse({'resourceArticle':article_id})
# 首页-资源-通过资源id查询文章
class showAllResourceArticleInfo(View):
    def get(self,request):
        a = request.GET.get('resourceData[]')
        if a==None:
            return JsonResponse({})
        a = tuple(map(int, a.strip('[]').split(',')))
        if len(a)==1:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleClassifyName,publishTime '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN ({a[0]})')
        else:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleClassifyName,publishTime '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN {a}')
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        articleInfo = []
        for row in rows:
            publishTime_str=row[4].strftime("%Y-%m-%d") if isinstance(row[4], datetime) else row[4]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[1],
                "articleImgLitimg": row[2].decode('utf-8') if isinstance(row[2], bytes) else row[2],
                "articleClassifyName": row[3],
                "publishTime": timestamp
            }
            articleInfo.append(info)
        return JsonResponse({'articleInfo':list(articleInfo)})
# 首页 -中间展示文章
class showAllMiddle(View):
    def get(self,request):
        cursor = connection.cursor()
        cursor.execute('SELECT allArticle '
                       'FROM systemsetup')
        allArticle_id = cursor.fetchone()
        cursor = connection.cursor()
        cursor.execute('SELECT stickArticle '
                       'FROM systemsetup')
        stickArticle_id = cursor.fetchone()
        return JsonResponse({'allArticle':allArticle_id,'stickArticle':stickArticle_id})
# 首页-置顶文章
class showAllTopArticleInfo(View):
    def get(self,request):
        a = request.GET.get('stickData[]')
        if a==None:
            return JsonResponse({})
        a = tuple(map(int, a.strip('[]').split(',')))
        if len(a)==1:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleClassifyName,publishTime '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN ({a[0]})')
        else:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleClassifyName,publishTime '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN {a}')
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        articleInfo = []
        for row in rows:
            publishTime_str=row[4].strftime("%Y-%m-%d") if isinstance(row[4], datetime) else row[4]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[1],
                "articleImgLitimg": row[2].decode('utf-8') if isinstance(row[2], bytes) else row[2],
                "articleClassifyName": row[3],
                "publishTime": timestamp
            }
            articleInfo.append(info)
        return JsonResponse({'articleInfo':list(articleInfo)})
# 首页-置顶下面-所有文章
class showAllArticleInfo(View):
    def get(self,request):
        a = request.GET.get('stickData[]')
        if a==None:
            sql = f"SELECT articleId,articleTitle,articleImgLitimg,articleDase,articleClassifyName,userName,publishTime,click,articleClassifyId FROM articleinfo"
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            articleInfo = []
            for row in rows:
                publishTime_str = row[6].strftime("%Y-%m-%d") if isinstance(row[6], datetime) else row[6]
                timestamp = time_handle(publishTime_str)
                info = {
                    "articleId": row[0],
                    "articleTitle": row[1],
                    "articleImgLitimg": row[2].decode('utf-8') if isinstance(row[2], bytes) else row[2],
                    "articleDase": row[3],
                    "articleClassifyName": row[4],
                    "userName": row[5],
                    "publishTime": timestamp,
                    "click": row[7],
                    'articleClassifyId':row[8]
                }
                articleInfo.append(info)
            # print(articleInfo)
            return JsonResponse({'articleInfo': list(articleInfo)})
        a = tuple(map(int, a.strip('[]').split(',')))
        if len(a)==1:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleDase,articleClassifyName,userName,publishTime,click,articleClassifyId '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN ({a[0]})')
        else:
            sql = (f'SELECT articleId,articleTitle,articleImgLitimg,articleDase,articleClassifyName,userName,publishTime,click,articleClassifyId '
                   f'FROM articleinfo '
                   f'WHERE articleId '
                   f'IN {a}')
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        articleInfo = []
        for row in rows:
            publishTime_str=row[6].strftime("%Y-%m-%d") if isinstance(row[6], datetime) else row[6]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[1],
                "articleImgLitimg": row[2].decode('utf-8') if isinstance(row[2], bytes) else row[2],
                "articleDase": row[3],
                "articleClassifyName": row[4],
                "userName": row[5],
                "publishTime": timestamp,
                "click": row[7],
                'articleClassifyId': row[8]
            }
            articleInfo.append(info)
        # print(articleInfo)
        return JsonResponse({'articleInfo':list(articleInfo)})
class showArticleCount(View):
    def get(self,request):
        # 向数据库中查询文章的总数量
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) '
                       'FROM articleinfo')
        article_count = cursor.fetchone()[0]
        return JsonResponse({'count':article_count})
# 精品文章
class showAllArticles(View):
    def get(self,request):
        currentPage = request.GET.get('currentPage') # 当前页
        # print(currentPage)
        start_index = (int(currentPage) - 1) * 8
        # print(start_index)
        pageSize = request.GET.get('pageSize') # 数据行数
        # print(pageSize)
        cursor = connection.cursor()
        cursor.execute(f'SELECT articleId, articleTitle, articleClassifyId, articleClassifyName, articleDase, articleImgLitimg, userName, publishTime, click '
                       f'FROM articleinfo '
                       f'LIMIT {start_index}, {pageSize}')
        rows = cursor.fetchall()
        articleInfo = []
        for row in rows:
            publishTime_str=row[7].strftime("%Y-%m-%d") if isinstance(row[7], datetime) else row[7]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[1],
                "articleImgLitimg": row[5].decode('utf-8') if isinstance(row[5], bytes) else row[5],
                "articleDase": row[4],
                "userName": row[6],
                "publishTime":timestamp ,
                "articleClassifyName": row[3],
                "click": row[8]
            }
            articleInfo.append(info)
        cursor = connection.cursor()
        cursor.execute(f'SELECT COUNT(*) '
                       f'FROM articleinfo ')
        count = cursor.fetchone()
        articleCount = count[0]
        data={'list': articleInfo,'total':articleCount,'pageSize':pageSize,'currentPage':currentPage}

        # print(articleCount)
        return JsonResponse({'data': data,'articleCount':articleCount})
class updateArticleClick(View):
    def get(self,request):
        articleId = request.GET.get('articleId')
        cursor = connection.cursor()
        cursor.execute(f'UPDATE articleinfo SET click=click+1,review = review+1 WHERE articleId={articleId}')
        cursor.fetchone()
        return JsonResponse({'data': 'ok'})
# 通过文章id详细显示文章内容
class articleDetails(View):
    def get(self,request):
        articleId = request.GET.get('articleId')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM articleinfo WHERE articleId={articleId}')
        row = cursor.fetchone()
        publishTime_str = row[9].strftime("%Y-%m-%d") if isinstance(row[9], datetime) else row[9]
        timestamp = time_handle(publishTime_str)
        info = {
            "articleId": row[0],
            "articleTitle": row[3],
            "articleImgLitimg": row[7].decode('utf-8') if isinstance(row[5], bytes) else row[5],
            "articleDase": row[6],
            'articleContent':row[8],
            "userName": row[2],
            "publishTime": timestamp,
            "articleClassifyName": row[5],
            "click": row[-2],
            'review':row[-1],
            'commentState':row[-3]
        }
        return JsonResponse({'data': info})
# 搜索
class searchShowAll(View):
    def get(self,request):
        keyword = request.GET.get('keyword')
        keyword = '%'+keyword+'%'
        currentPage = request.GET.get('currentPage') # 当前页
        # print(currentPage)
        start_index = (int(currentPage) - 1) * 8
        # print(start_index)
        pageSize = request.GET.get('pageSize') # 数据行数
        # print(pageSize)
        cursor = connection.cursor()
        cursor.execute(f"SELECT articleId, articleTitle, articleClassifyId, articleClassifyName, articleDase, articleImgLitimg, userName, publishTime, click FROM articleinfo WHERE articleContent  LIKE '{keyword}' LIMIT {start_index}, {pageSize}")
        rows = cursor.fetchall()

        articleInfo = []
        for row in rows:
            publishTime_str=row[7].strftime("%Y-%m-%d") if isinstance(row[7], datetime) else row[7]
            timestamp = time_handle(publishTime_str)
            info = {
                "articleId": row[0],
                "articleTitle": row[1],
                "articleImgLitimg": row[5].decode('utf-8') if isinstance(row[5], bytes) else row[5],
                "articleDase": row[4],
                "userName": row[6],
                "publishTime":timestamp ,
                "articleClassifyName": row[3],
                "click": row[8]
            }
            articleInfo.append(info)
        cursor = connection.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM articleinfo WHERE articleContent LIKE '%{keyword}%'")
        count = cursor.fetchone()
        articleCount = count[0]
        data={'list': articleInfo,'total':articleCount,'pageSize':pageSize,'currentPage':currentPage}
        # print(data)
        # print(articleCount)
        return JsonResponse({'data': data,'articleCount':articleCount})
# 文章中的评论区  -当前文章id   返回评论区数据
class showCommentByArticleId(View):
    def get(self, request):
        # 当前文章id
        articleId = request.GET.get('articleId')

        # 查询评论区数据
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT
              t1.userId,
              t2.username AS userName,
              t2.userIcon,
              t1.content,
              t1.commentDate,
              t1.commentId,
              COALESCE(t3.children, '[]') AS child
            FROM
              commentinfo t1
              INNER JOIN userinfo t2 ON t1.userId = t2.userId
              LEFT JOIN (
                SELECT
                  parentId,
                  JSON_ARRAYAGG(
                    JSON_OBJECT(
                      'userId', t4.userId,
                      'userName', t5.username,
                      'userIcon', t5.userIcon,
                      'content', t4.content,
                      'commentDate', t4.commentDate,
                      'commentId', t4.commentId,
                      'child', '[]'
                    )
                  ) AS children
                FROM
                  commentinfo t4
                  INNER JOIN userinfo t5 ON t4.userId = t5.userId
                WHERE
                  t4.parentId != 0
                GROUP BY
                  t4.parentId
              ) t3 ON t1.commentId = t3.parentId
            WHERE
              t1.articleId = {articleId} AND t1.parentId = 0
        """)
        rows = cursor.fetchall()
        # print(rows)
        # 构建评论区数据结构
        result = []
        for row in rows:
            userId, userName, userIcon, content, commentDate, commentId, child = row
            data = {
                'userName': userName,
                'userId': userId,
                'userIcon': userIcon,
                'content': content,
                'commentDate': commentDate.strftime('%Y-%m-%d'),
                'commentId': commentId,
                'child': json.loads(child)
            }
            result.append(data)

        return JsonResponse({'commentInfo': result})

class insertCommentInfo(View):
    def post(self,request):
        json_data = json.loads(request.body)
        articleId = json_data.get('articleId')
        print(articleId)
        userId = json_data.get('userId')
        print(userId)
        content = json_data.get('content')
        print(content)
        parentId = json_data.get('parentId')
        print(parentId)
        cursor = connection.cursor()
        sql = f"INSERT INTO commentinfo (articleId, userId, content, parentId) VALUES ({articleId},{userId},'{content}',{parentId})"
        cursor.execute(sql)
        return JsonResponse({'code': 0})
class deleteCommentInfo(View):
    def delete(self,request):
        # 获取传递的参数
        comment_id = request.GET.get("commentId")
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM commentinfo WHERE commentId={comment_id}")
        if cursor.rowcount > 0:  # 判断是否有数据被删除
            return JsonResponse({'code': 0})  # 成功删除返回 0
        else:
            return JsonResponse({'code': 1, 'msg': 'No rows deleted'})  # 没有数据被删除返回 1
# 学习网站
class showAllUrlInfo(View):
    def get(self,request):
        urlType = request.GET.get('urlType')
        cursor=connection.cursor()
        cursor.execute(f"SELECT * FROM urlinfo WHERE urlType={urlType}")
        rows = cursor.fetchall()
        urlList = []
        for row in rows:
            info={
                'urlId':row[0],
                'urlName': row[1],
                'urlAddres': row[2],
                'urlReferral': row[3],
                'urlLitimg': row[4],
                'webmasterEmail': row[5],
                'urlPass': row[6],
                'urlType': row[7],
            }
            urlList.append(info)
        return JsonResponse({'data': urlList})
    def post(self,request):
        json_data = json.loads(request.body)
        urlName = json_data.get('urlName')
        # print(urlName)
        urlAddres = json_data.get('urlAddres')
        # print(urlAddres)
        urlReferral = json_data.get('urlReferral')
        # print(urlReferral)
        urlLitimg = json_data.get('urlLitimg')
        # print(urlLitimg)
        webmasterEmail = json_data.get('webmasterEmail')
        # print(webmasterEmail)
        cursor = connection.cursor()
        sql = "INSERT INTO commentinfo (urlName, urlAddres, urlReferral, urlLitimg, webmasterEmail) VALUES (%s, %s, %s, %s, %s)"
        params = [urlName, urlAddres, urlReferral, urlLitimg, webmasterEmail]
        cursor.execute(sql, params)
        return JsonResponse({'code': 0})
class fileUpload(View):
    def post(self, request):
        file = request.FILES.get('file')  # 获取上传的文件对象
        file_path = os.path.join('dist', 'userIcon', file.name)  # 拼接文件保存路径
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # 如果文件夹不存在，就创建文件夹
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)  # 保存文件

        return JsonResponse({'status': 'success', 'path': file_path})  # 返回保存成功的文件路径


class showAllSystemSetup(View, Cursor):
    def get(self, request):
        sql = f"SELECT * FROM systemsetup"
        row = self.Fetchone(sql)

        info = {
            'effects02': row[0],
            'effects01': row[1],
            'stickArticle': row[2],
            'allArticle': row[3],
            'featuredArticle': row[4],
            'technologyArticle': row[5],
            'resourceArticle': row[6],
            'advertising1': row[7],
            'advertisingLink1': row[8],
            'advertising2': row[9],
            'advertisingLink2': row[10],
            'advertising3': row[11],
            'advertisingLink3': row[12]
        }

        response = JsonResponse(info)
        response["Access-Control-Allow-Origin"] = "*"  # 设置允许所有源访问

        return response