from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from datetime import datetime

def post_page(request, pk):
    print(request)
    print(request.user)
    user_is_publisher = False
    post = Post.objects.filter(pk=pk).first()
    user_is_ANN = True
    if request.user.is_authenticated:
        user_is_ANN = False
        user = request.user
        profile = Profile.objects.filter(user = user).first()
        

        print(post.profile)
        print(post.profile.user == profile.user)

        if profile.user == post.profile.user:
            print("same")
            user_is_publisher = True

    context = { 'post' : post,
                'user_is_publisher' : user_is_publisher }
    
    if request.method == "POST":
        print(request.POST)

        #delete btn
        if "del" in request.POST:
            post.delete()
            return redirect(main_page)
            
        
        print("################")

        if "likebtn" in request.POST:
            if user_is_ANN == False:
                #check Like status
                like_info = Like.objects.filter(post=post, profile = profile).first()
                print(like_info)
                if like_info:
                    post.likecount -= 1
                    post.save()
                    like_info.delete()
                    pass
                else:
                    post.likecount += 1
                    post.save()
                    Like.objects.create(post = post, profile = profile)



                

            pass
        #like btn 2 like
        #like btn 2 cancel
        

        





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
            Post.objects.create(profile = profile, image = request.FILES.get("chooseFile"))
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
    
    sort_field = '-likecount'
    total = ''
    if request.method == "POST":
        print(request.POST)
        if 'my_page' in request.POST:
            return redirect('account/my_page/'+str(user.id))

        sortoption = request.POST.get("sortoption")
        print(sortoption)
        match sortoption:
            case 'most_like':
                sort_field = '-likecount'
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
    #filtered_posts = [post for post in posts if post.likecount > 10]
    print(posts)
    context = {'posts' : posts}
    return render(request, 'main_page.html',context)