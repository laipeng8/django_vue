# !/user/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from .views import (showUserEmail,showUserName,sendEmail,insertRegisterInfo,loginShowAllUserInfo
                    ,insertLoginInfo,showUserNameOrEmail,sendEmailReset,updateUserPass)


urlpatterns = [
    # path('showAllFeaturedArticleInfo', showAllFeaturedArticleInfo.as_view()),
    path('register/showUserEmail', showUserEmail.as_view()),
    path('register/showUserName', showUserName.as_view()),
    path('sendEmail', sendEmail.as_view()),
    path('register/insertRegisterInfo', insertRegisterInfo.as_view()),
    path('login/showAllUserInfo', loginShowAllUserInfo.as_view()),
    path('login/insertLoginInfo', insertLoginInfo.as_view()),
    path('resetPassword/showUserNameOrEmail', showUserNameOrEmail.as_view()),
    path('sendEmailReset', sendEmailReset.as_view()),
    path('resetPassword/updateUserPass', updateUserPass.as_view()),
    # ...
]
