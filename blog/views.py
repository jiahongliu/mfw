from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models

def index(request):
    travels=models.Travel.objects.all()
    pindex=request.GET.get("pindex")#设置分页展示

    pageinator=Paginator(travels, 20)
    if pindex==""or pindex==None:
        pindex=1
    page=pageinator.page(pindex)

    print(page.paginator.count)
    return render(request,'blog/index.html',{'page':page})

def article_page(request,article_id):
    acticle=models.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

# def travel(request):
#     travel_pp=models.Travel.objects.get(pk=1)
#     return render(request,'blog/index.html',{'travel_pp':travel_pp})
