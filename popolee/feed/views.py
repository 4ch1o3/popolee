from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from datetime import datetime


def main_page(request):
    print(request)
    #exchange_info = Exchange.objects.all().values()[0]
    user_pk = request.user.pk
    user = User.objects.get(id=user_pk)
    context = {'info' : exchange_info,
               'user' : user}
    return render(request, 'main_page.html',context)