from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('Hello, World')

def settingPageView(request):
    return HttpResponse("Add settings")