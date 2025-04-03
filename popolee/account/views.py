from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from datetime import datetime

# Create your views here.
def login_page(request):
    print("this is login_page")
    print(request)

    if request.method == "POST":
        userid = request.POST.get("username")
        pwd = request.POST.get("password")
        print(userid)
        print(pwd)
        user = auth.authenticate(request, username = userid, password = pwd)
        print(user)
        #user = User.objects.get(username = userid)

        if user is not None:
            auth.login(request, user)
            print(user.pk)
        else:
            print("Wrong id or pwd")


    return render(request, 'login_page.html')