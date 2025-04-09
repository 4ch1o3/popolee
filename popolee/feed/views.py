from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from datetime import datetime

def post_page(request, pk):
    print(request)
    context = {}

    #check user
    requester_profile = None
    if request.user.is_authenticated == True:
        check_profile = Profile.objects.filter(user=request.user).first()
        if check_profile:
            requester_profile = check_profile
    context["requester_profile"] = requester_profile

    #show post
    post = Post.objects.filter(pk=pk).first()
    context['post'] = post

    #check publisher and requester
    if post.profile == requester_profile:
        user_is_publisher = True
    else:
        user_is_publisher = False
    context["user_is_publisher"] = user_is_publisher

    
    if request.method == "POST":
        print(request.POST)

        #feat : delete the post
        if "del" in request.POST:
            post.delete()
            return redirect("feed:main_page")
            
        
        #feat : like btn
        if "likebtn" in request.POST:
            #Anonymous user -> login to like
            if requester_profile == None:
                return redirect('account:login_page')
            else:
                #check Like status (search in Like DB)
                like_info = Like.objects.filter(post=post, profile = requester_profile).first()
                
                #like cancel
                if like_info:
                    post.likecount -= 1
                    post.save()
                    like_info.delete()

                #like confirm
                else:
                    post.likecount += 1
                    post.save()
                    Like.objects.create(post = post, profile = requester_profile)


    return render(request, 'post_page.html' ,context)

def upload_page(request):
    print(request)
    context = {}

    #check user
    requester_profile = None
    if request.user.is_authenticated == True:
        check_profile = Profile.objects.filter(user=request.user).first()
        if check_profile:
            requester_profile = check_profile
    context["requester_profile"] = requester_profile

    #Anonymous user -> login
    if requester_profile == None:
        return redirect('account:login_page')
    
    
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        print("####")

        #upload img file (create Post model record)
        if request.FILES.get("upload_img"):
            Post.objects.create(profile = requester_profile, image = request.FILES.get("upload_img"))
            return redirect("feed:main_page")

    
    return render(request, 'upload_page.html',context)

def main_page(request):
    print(request)
    context = {}

    #check user
    requester_profile = None
    if request.user.is_authenticated == True:
        check_profile = Profile.objects.filter(user=request.user).first()
        if check_profile:
            requester_profile = check_profile
    context["requester_profile"] = requester_profile


    #show feed(default)
    max_images = 10     
    posts = Post.objects.order_by('-likecount')[:max_images]


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

        #feat : tag options(headcount)
        tag = request.POST.get("headcount")

        if tag != '':
            posts = Post.objects.filter(headcount = tag).order_by(sort_field)[:max_images]  
        else:
            posts = Post.objects.order_by(sort_field)[:max_images]

    context["posts"] = posts

    return render(request, 'main_page.html',context)