from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from . models import memory
from notes.views import show

    
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect(show)
        else:
            return render(request,'home.html',{'error':"login is not available"})
    else:
        return render(request,'home.html')
    
    
def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['passwordagain']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'register.html',{'error':'username has already exit'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
               
            
                auth.login(request,user)
                return redirect(home)
                
            
        else:
            return render(request,'register.html',{'error':'password dont match'})
      
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect(home)

# Create your views here.
