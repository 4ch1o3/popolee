from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #For First Page & Login
    path('',views.main_page,name="main_page"),
    path('upload',views.upload_page,name="upload_page"),

    
    
]