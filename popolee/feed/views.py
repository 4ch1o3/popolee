from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from datetime import datetime

max_images = 10

def main_page(request): #show images
    print(request)
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
        posts = Image.objects.order_by(sort_field)[:max_images]

    #exchange_info = Exchange.objects.all().values()[0]
    posts = Image.objects.order_by('likes')[:max_images]
    print(posts)
    context = {'posts' : posts}
    return render(request, 'main_page.html',context)