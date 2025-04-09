from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from datetime import datetime

# Create your views here.
def my_page(request, pk):
    return render(request, 'my_page.html')

def login_page(request):
    print("this is login_page")
    print(request)

    if request.method == "POST":
        userid = request.POST.get("id")
        pwd = request.POST.get("pwd")
        print(userid)
        print(pwd)
        user = auth.authenticate(request, username = userid, password = pwd)
        print(user)
        #user = User.objects.get(username = userid)

        if user is not None:
            auth.login(request, user)
            print(user.pk)
            return redirect('main_page')
        else:
            print("Wrong id or pwd")


    return render(request, 'login_page.html')


from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

def register_page(request):
    print("this is register_page")
    print(request)
    context = {}

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            print(user.username)
            Profile.objects.create(user=user, nickname = user.username)
            return redirect('login_page')  # 회원가입 후 로그인 페이지 등으로 리디렉션
    else:
        form = CustomUserCreationForm()
    return render(request, 'register_page.html', {'form': form})