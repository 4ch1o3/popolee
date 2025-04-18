from django.urls import path
from . import views
from .api_views import *
from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    path('login',views.login_page,name="login_page"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register',views.register_page,name="register_page"),
    path('my_page/<int:pk>',views.my_page,name="my_page"),

    #api
    #path('api/auth/regist', Api_regist.as_view(), name='api_regist'),
    #path('api/auth/login', Api_login.as_view(), name='api_login'),
    #path('api/auth/logout', Api_logout.as_view(), name='api_logout'),
    #path('api/view/feed', Api_feed.as_view(), name='api_feed'),
]