from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models

def index(request):
    travels=models.Travel.objects.all()
    return render(request,'blog/index.html',{'travels':travels})

def article_page(request,article_id):
    acticle=models.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

# def travel(request):
#     travel_pp=models.Travel.objects.get(pk=1)
#     return render(request,'blog/index.html',{'travel_pp':travel_pp})