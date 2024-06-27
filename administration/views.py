from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import WritingSubmission


def index(request):
    return render(request,'admin_dashboard.html')

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
            return redirect('submission_success')  # Ensure this URL exists
        else:
            return HttpResponse("All fields are required.", status=400)

    return render(request, 'submit_writing.html')

def submission_success(request):
    return render(request, 'submission_success.html')


@login_required
def submission_history(request):
    submissions = WritingSubmission.objects.filter(user=request.user)
    return render(request, 'administration/submission_history.html', {'submissions': submissions})
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WritingSubmission

@login_required
def submission_detail(request, submission_id):
    submission = get_object_or_404(WritingSubmission, id=submission_id)
    return render(request, 'administration/submission_detail.html', {'submission': submission})


