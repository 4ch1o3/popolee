from .models import *
from feed.models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from datetime import datetime

# Create your views here.
def my_page(request, pk):
    print(request)
    context = {}

    #check user
    requester_profile = None
    if request.user.is_authenticated == True:
        check_profile = Profile.objects.filter(user=request.user).first()
        if check_profile:
            requester_profile = check_profile
    context["requester_profile"] = requester_profile

    #get page_owner
    page_owner = Profile.objects.filter(id = pk).first()
    print(page_owner)

    #show posts
    posts = Post.objects.filter(profile = page_owner).order_by('-likecount')

    if request.method == "POST":
        print(request.POST)

        #feat : sort options
        sortoption = request.POST.get("sortoption")
        match sortoption:
            case 'most_like':
                sort_field = '-likecount'
            case 'show_old':
                sort_field = 'created_at'
            case 'show_new':
                sort_field = '-created_at'
        posts = Post.objects.filter(profile = page_owner).order_by(sort_field)
    
    context['posts'] = posts

    return render(request, 'my_page.html', context)

def login_page(request):
    print(request)
    context = {}

    err_state = False

    if request.method == "POST":
        userid = request.POST.get("id")
        pwd = request.POST.get("pwd")

        #find user with userid and pwd
        user = auth.authenticate(request, username = userid, password = pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('feed:main_page')
        #login fail
        else:
            err_state = True

    context["err_state"] = err_state
    context["err"] = "Wrong id or password, Try again"

    return render(request, 'login_page.html', context)


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
            return redirect('account:login_page')  # 회원가입 후 로그인 페이지 등으로 리디렉션
    else:
        form = CustomUserCreationForm()
    return render(request, 'register_page.html', {'form': form})