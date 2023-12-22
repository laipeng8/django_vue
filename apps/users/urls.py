from django.urls import path
# 子路由

from django.urls import path
from . import views

urlpatterns = [
    # 判断用户名是否重复
    path('username/', views.UsernameCountView.as_view()),
    path('mobile/',views.MobileCountView.as_view()),
    path('register/',views.RegisterView.as_view()),
    path('mobilecode/',views.SMSCodeView.as_view()),#get的生成验证码-注册
    path('login/',views.LoginView.as_view()),#post的登录
    path('logincode/',views.LoginCodeView.as_view()),#get的生成验证码-短信登录
    path('translate/',views.translator.as_view()),#翻译
    path('logout/',views.LogoutView.as_view()),#退出登录

]

