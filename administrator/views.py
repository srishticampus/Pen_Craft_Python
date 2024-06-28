from django.shortcuts import render,redirect
from pen.models import Master,User
from django.contrib.auth.models import User
# Create your views here.

def adminmaster(request):
    msg = ''
    data = Master.objects.all()
    return render(request, 'adminmaster/adminmaster.html', {"data": data, "msg": msg})

def approvemaster(request):
    id = request.GET['id']
    status = request.GET['status']
    data = User.objects.get(id=id)
    data.is_active = status == 1
    data.save()
    return redirect("/adminmaster")