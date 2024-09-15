# !/backstage/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
# 子路由

from django.urls import path
from . views import (showAllClassifyInfo,showArticleCount,showUserCount,CommentCount,thumbnailUpload,insertArticleInfo,
                     updateArticleNumberByClassifyId,articleManage,articleSearchTitle,articleSearchPass,
                     commentManager,updateUserBasicsInfo,updateUserEmail,updateUserPass,classifyManager,
                     userManager,linkManage,auditScreening)

urlpatterns = [
    path('showAllClassifyInfo', showAllClassifyInfo.as_view()),
    path('user/showUserCount',showUserCount.as_view()),
    path('article/showArticleCount',showArticleCount.as_view()),
    path('comment/count',CommentCount.as_view()),
    path('thumbnailUpload',thumbnailUpload.as_view()),
    path('article/insertArticleInfo',insertArticleInfo.as_view()),
    path('updateArticleNumberByClassifyId',updateArticleNumberByClassifyId.as_view()),
    path('article/page/byUserType',articleManage.as_view()),
    path('article/search/title',articleSearchTitle.as_view()),
    path('article/search/pass',articleSearchPass.as_view()),
    path('comment/page/byUserType', commentManager.as_view()),
    path('user/updateUserBasicsInfo', updateUserBasicsInfo.as_view()),
    path('user/updateUserEmail', updateUserEmail.as_view()),
    path('user/updateUserPass', updateUserPass.as_view()),
    path('classifyManager', classifyManager.as_view()),
    path('user/page/findby', userManager.as_view()),
    path('url/page/findby', linkManage.as_view()),
    path('url/page/findby', auditScreening.as_view()),

]