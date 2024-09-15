# !/backstage/bin/env python3
# -*- coding: utf-8 -*-
# urls.py
#
from django.urls import path
from .views import (showArticleCount,showAllFeaturedArticleInfo,
                    showAllFeatured,
                    showAllArticles,showClassifyInfoByClassifyId,
                    byClassifyId,showAllTechnology,showAllTechnologyArticleInfo,
                    showAllResource,showAllResourceArticleInfo,
                    showAllMiddle,showAllTopArticleInfo,showAllArticleInfo,
                    articleDetails,updateArticleClick,
                    searchShowAll,showCommentByArticleId,
                    insertCommentInfo,deleteCommentInfo,showAllUrlInfo,
                    fileUpload,showAllSystemSetup,)

urlpatterns = [
    path('showAllFeaturedArticleInfo', showAllFeaturedArticleInfo.as_view()),
    path('showAllFeatured', showAllFeatured.as_view()),
    path('article/showArticleCount', showArticleCount.as_view()),
    path('article/page/showAll', showAllArticles.as_view()),
    path('classify/showClassifyInfoByClassifyId',showClassifyInfoByClassifyId.as_view()),
    path('article/byClassifyId',byClassifyId.as_view()),
    path('showAllTechnology',showAllTechnology.as_view()),
    path('showAllTechnologyArticleInfo',showAllTechnologyArticleInfo.as_view()),
    path('showAllResource', showAllResource.as_view()),
    path('showAllResourceArticleInfo', showAllResourceArticleInfo.as_view()),
    path('showAllMiddle', showAllMiddle.as_view()),
    path('showAllTopArticleInfo', showAllTopArticleInfo.as_view()),
    path('showAllArticleInfo', showAllArticleInfo.as_view()),
    path('article/showArticleInfo', articleDetails.as_view()),
    path('article/updateArticleClick', updateArticleClick.as_view()),
    path('article/page/searchShowAll', searchShowAll.as_view()),
    path('showCommentByArticleId', showCommentByArticleId.as_view()),
    path('comment/insertCommentInfo', insertCommentInfo.as_view()),
    path('comment/delete', deleteCommentInfo.as_view()),
    path('url/showAllUrlInfo', showAllUrlInfo.as_view()),
    path('fileUpload', fileUpload.as_view()),
    path('showAllSystemSetup', showAllSystemSetup.as_view()),
    # ...
]
