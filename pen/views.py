# views.py
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserReg, Master

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'landing_page.html')

def registration(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        qualification = request.POST['qualification']
        phone_number = request.POST['phone_number']
        location = request.POST['location']
        state = request.POST['state']
        city = request.POST['city']
        image = request.FILES['image']

        try:
            usr = User.objects.create_user(
                username=email, password=password, is_active=1)
            usr.save()
            par = UserReg.objects.create(
                                        email=email,address=address, user=usr,qualification=qualification,
                                                     phone_number=phone_number,location=location, state=state, city=city, image=image)
            par.save()
            return redirect('/login')
        except:
            msg = 'Something went wrong..'
            return render(request, 'registration.html')

    else:
        return render(request, 'registration.html', {"msg": msg})


def login_user(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_superuser:
                return redirect("admin:index")
            elif user.is_staff:
                data = Master.objects.get(email=email)
                request.session['id'] = data.id
                return redirect("home")
            else:
                data = UserReg.objects.get(email=email)
                request.session['id'] = data.id
                return redirect("home")
        else:
            msg = 'Please check the email..'
            return render(request, 'login.html', {"msg": msg})
    else:
        return render(request, 'login.html')

    

def coReg(request):
    msg = ''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        qual = request.POST['qual']
        field = request.POST['field']
        img = request.FILES['proof']
        try:
            usr = User.objects.create_user(
                username=email, password=password, is_active=0, is_staff=1)
            usr.save()
            tut = Master.objects.create(name=name, email=email, phone=phone, address=address,
                                       qual=qual, field=field, img=img, user=usr)
            tut.save()
            msg = 'Registration Succesful..'
        except:
            msg = 'Something went wrong..'
    data = Master.objects.all()
    return render(request, 'coReg.html', {"data": data, "msg": msg})

# def admintutors(request):
#     msg = ''
#     data = Master.objects.all()
#     return render(request, 'admintutors.html', {"data": data, "msg": msg})

# def approvetutor(request):
#     id = request.GET['id']
#     status = request.GET['status']
#     data = User.objects.get(id=id)
#     data.is_active = status
#     data.save()
#     return redirect("/admintutors")

@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')
