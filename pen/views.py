# views.py
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserReg

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'landing_page.html')

def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        qualification = request.POST.get('qualification')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        location = request.POST.get('location')
        state = request.POST.get('state')
        city = request.POST.get('city')
        image = request.FILES.get('image')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password do not match!")
        
        try:
            my_user = User.objects.create_user(username=username, email=email, password=pass1)

            user_reg = UserReg.objects.create(
                user=my_user,
                qualification=qualification,
                phone_number=phone_number,
                address=address,
                location=location,
                state=state,
                city=city,
                image=image
            )

            return redirect('login')

        except Exception as e:
            return HttpResponse(f"Error creating user: {e}")

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')
