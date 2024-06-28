from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserReg, Master, WritingSubmission

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'landing_page.html')

def registration(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        password = request.POST['password']
        password1 = request.POST['password1']
        qualification = request.POST['qualification']
        phone_number = request.POST['phone_number']
        location = request.POST['location']
        state = request.POST['state']
        city = request.POST['city']
        image = request.FILES['image']

        if password != password1:
            return HttpResponse("Your password and confirm password do not match!")

        try:
            usr = User.objects.create_user(
                username=username, password=password, is_active=1)
            usr.save()
            par = UserReg.objects.create(
                user=usr, address=address, qualification=qualification,
                phone_number=phone_number, location=location, state=state, city=city, image=image)
            par.save()
            return redirect('login')  # Use named URL
        except:
            msg = 'Something went wrong..'
    return render(request, 'registration.html', {"msg": msg})

def login_user(request):
    msg = ''
    next_url = request.GET.get('next', 'home') 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("admin:index")
            elif user.is_staff:
                data = Master.objects.get(user=user)
                request.session['id'] = data.id
                return redirect(next_url)  # Redirect to next URL or home
            else:
                data = UserReg.objects.get(user=user)
                request.session['id'] = data.id
                return redirect(next_url)  # Redirect to next URL or home
        else:
            msg = 'Invalid email or password.'
    return render(request, 'login.html', {"msg": msg})

def coReg(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        qual = request.POST['qual']
        field = request.POST['field']
        img = request.FILES['img']
        try:
            usr = User.objects.create_user(
                username=username, password=password, is_active=0, is_staff=1)
            usr.save()
            tut = Master.objects.create(username=username, email=email, phone=phone, address=address,
                                        qual=qual, field=field, img=img, user=usr)
            tut.save()
            msg = 'Registration Successful..'
        except:
            msg = 'Something went wrong..'
    data = Master.objects.all()
    return render(request, 'coReg.html', {"data": data, "msg": msg})

def adminmaster(request):
    msg = ''
    data = Master.objects.all()
    return render(request, 'adminmaster.html', {"data": data, "msg": msg})

def approvemaster(request):
    id = request.GET['id']
    status = request.GET['status']
    data = User.objects.get(id=id)
    data.is_active = status
    data.save()
    return redirect("adminmaster")

@login_required
def submit_writing(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')

        if category and title and description and file:
            submission = WritingSubmission(
                user=request.user,
                category=category,
                title=title,
                description=description,
                file=file
            )
            submission.save()
            return redirect('home')  # Ensure this URL exists
        else:
            return HttpResponse("All fields are required.", status=400)

    return render(request, 'submit_writing.html')


@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')
