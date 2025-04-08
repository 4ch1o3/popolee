from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from datetime import datetime

def post_page(request, pk):
    print(request)
    post = Post.objects.filter(pk=pk).first()
    context = { 'post' : post }



    return render(request, 'post_page.html' ,context)

def upload_page(request):
    print(request)
    print(request.user.is_authenticated)

    if request.user.is_authenticated == False:
        return redirect('login_page')
    
    else:
        print(request.user)
    
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        print("####")
        user = request.user
        profile = Profile.objects.filter(user = user).first()
        print(user)
        print(profile)
        if request.FILES.get("chooseFile"):
            Post.objects.create(publisher = profile, image = request.FILES.get("chooseFile"))
            return redirect(main_page)

    
    return render(request, 'upload_page.html')

def main_page(request): #show images
    print(request)
    context = {}

    if request.user.is_authenticated == True:
        user = Profile.objects.filter(user=request.user)
        print(user)
        context["user"] = user
        
    max_images = 10     
    
    sort_field = '-likes'
    total = ''
    if request.method == "POST":
        print(request.POST)

        sortoption = request.POST.get("sortoption")
        print(sortoption)
        match sortoption:
            case 'most_like':
                sort_field = '-likes'
            case 'show_old':
                sort_field = 'created_at'
            case 'show_new':
                sort_field = '-created_at'

        males = females = int(0)
        in_male = request.POST.get("in_male")
        in_female = request.POST.get("in_female")
        if in_male != '':
            males = int(in_male)
        if in_female != '':
            females = int(in_female)
        #print(males, type(males))

        total = request.POST.get("headcount")
    
    print(total)
    
    if total != '':
        posts = Post.objects.filter(headcount = total).order_by(sort_field)[:max_images]

    else:
        posts = Post.objects.order_by(sort_field)[:max_images]
    #filtered_posts = [post for post in posts if post.likes > 10]
    print(posts)
    context = {'posts' : posts}
    return render(request, 'main_page.html',context)