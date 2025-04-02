from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from datetime import datetime


def main_page(request): #show images
    print(request)
    #exchange_info = Exchange.objects.all().values()[0]
    posts = Image.objects.order_by('created_at')[:30]
    print(posts)
    context = {'posts' : posts}
    return render(request, 'main_page.html',context)