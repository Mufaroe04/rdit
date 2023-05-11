from django.shortcuts import render,render
from app.models import *
from django.db.models import Count
def home(request):
    blogs=Blog.objects.annotate(comments_count=Count('comment'))
    context={
        'blogs':blogs
    }
    return render(request,'website/index.html',context)

