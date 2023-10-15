from django.shortcuts import render
from accounts.models import memory
from django.contrib.auth.models import User

def show(request):
    log=request.user
    memories=memory.objects.filter(user=log)
    return render(request,'showdiary.html',{'m':memories})

def add(request):
    if request.method=='POST':
        data=request.POST['data']
        new=memory(content=data,user=request.user)
        new.save()
        return render(request,'addmemory.html')
    else:
         return render(request,'addmemory.html')

# Create your views here.
