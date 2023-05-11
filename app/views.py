from django.shortcuts import render
from django.shortcuts import render ,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.hashers import make_password
def login(request):
    if request.method=='POST':
        username=request.POST['username'].strip()
        password=request.POST['password'].strip()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login')
    else:
        return render(request,'app/login.html')
# @login_required(login_url='login/')
def  logout(request):
     auth.logout(request)
     return redirect('login')

def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.password=make_password(new.password)
            new.save()
            login(request,new)
            return redirect('home')
    else:
        context={'form':form}
        return render(request,'app/register.html',context)
# read, admin, delete: Blog, Comment, User
def blog(request):
    form=BlogForm()
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.save()
            return  redirect('home')
    else :
        context={'form':form}
        return render(request,'app/blog.html',context)
def Admin(request):
    posts=Blog.objects.filter(created_by=request.user)
    context={'posts':posts}
    return render(request,'app/admin.html',context)
def delete(request,pk):
    obj=Blog.objects.get(id=pk)
    if request.method=="POST":
        obj.delete()
        return redirect('home')
    context={ 'obj': obj}
    return render(request,'app/delete.html',context)  
def update_blog(request,pk):
    blog=Blog.objects.get(id=pk) 
    form=BlogForm(instance=blog)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'app/update_blog.html',context)
def profile(request):
    user=User.objects.get(id=request.user.id )
    form=UserForm(instance=user)
    if request.method=='POST':
        form=UserForm(request.POST,request.FILES,instance=user)

        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'app/profile.html',context)
def read(request,pk):
    blog=Blog.objects.get(id=pk)
    comments=Comment.objects.filter(blog_commented=blog)
    if request.method=='POST':
        comment=Comment.objects.create(
             comment_by=request.user,blog_commented=blog,
            comment_body=request.POST.get('comment'),)
        return redirect('read',pk=blog.id)
    context={'blog':blog,'comments':comments}
    return render(request,'app/read.html',context)
