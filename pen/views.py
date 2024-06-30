import os
import nltk
import spacy
import requests
from bs4 import BeautifulSoup
import language_tool_python
from textstat import textstat
from spellchecker import SpellChecker
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import WritingSubmission

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserReg, Master, WritingSubmission
import chardet


from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserReg, Master, WritingSubmission,FeedbackDetails
import chardet
from django.http import JsonResponse
from django.contrib import messages


# Initialize tools
spell = SpellChecker()
tool = language_tool_python.LanguageTool('en-US')
nlp = spacy.load('en_core_web_sm')

# Known proper nouns
known_proper_nouns = {'Mr.', 'Mrs.', 'Miss', 'Ms.', 'Dr.', 'Emily', 'Blackwood', 'mid-flight',
                      'John', 'Mary', 'London', 'Paris', 'iPhone', 'Google', 'Python',
                      'January', 'Friday', 'Monday', 'Microsoft', 'Apple', 'Android'}

def preprocess_text(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    return sentences, words

def identify_proper_nouns(text):
    doc = nlp(text)
    proper_nouns = [ent.text for ent in doc.ents]
    return proper_nouns

def check_spelling(words, proper_nouns):
    misspelled_words = []
    for word in words:
        if word not in proper_nouns and word not in known_proper_nouns and not spell.correction(word.lower()) == word.lower():
            misspelled_words.append(word)
    return len(misspelled_words), misspelled_words

def check_grammar_and_quotation(sentences):
    grammar_errors = 0
    quotation_issues = []
    error_details = []

    for sentence in sentences:
        matches = tool.check(sentence)
        grammar_errors += len(matches)
        for match in matches:
            error_details.append({
                'sentence': sentence,
                'error': match.message,
                'suggestions': match.replacements
            })

        open_quote = False
        for i, char in enumerate(sentence):
            if char == '"':
                if not open_quote:
                    open_quote = True
                    start_index = i
                else:
                    open_quote = False
                    end_index = i
                    quoted_text = sentence[start_index:end_index+1]
                    quotation_issues.append((quoted_text, start_index, end_index))

        if open_quote:
            quotation_issues.append(("Unclosed quotation mark", len(sentence)-1, len(sentence)-1))

    return grammar_errors, error_details, quotation_issues

def calculate_readability(text):
    return textstat.flesch_kincaid_grade(text)

def check_plagiarism_online(sentence):
    query = f'"{sentence}"'
    url = f"https://www.google.com/search?q={requests.utils.quote(query)}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = soup.find_all('div', class_='yuRUbf')
    return len(results) > 0

def score_text(text):
    sentences, words = preprocess_text(text)
    proper_nouns = identify_proper_nouns(text)
    
    spelling_errors, misspelled_words = check_spelling(words, proper_nouns)
    grammar_errors, grammar_details, quotation_issues = check_grammar_and_quotation(sentences)
    readability_score = calculate_readability(text)
    
    plagiarism_matches = 0
    for sentence in sentences:
        if check_plagiarism_online(sentence):
            plagiarism_matches += 1
    
    plagiarism_percentage = (plagiarism_matches / len(sentences)) * 100
    
    initial_score = 10.0
    spelling_deduction = spelling_errors * 0.5
    score = initial_score - spelling_deduction

    grammar_deduction = grammar_errors * 0.5
    score -= grammar_deduction

    readability_deduction = readability_score * 0.1
    score -= readability_deduction

    plagiarism_deduction = plagiarism_percentage * 0.1
    score -= plagiarism_deduction

    score = max(0, score)

    return {
        "total_score": score,
        "spelling_errors": spelling_errors,
        "misspelled_words": misspelled_words,
        "grammar_errors": grammar_errors,
        "grammar_details": grammar_details,
        "readability_score": readability_score,
        "plagiarism_percentage": plagiarism_percentage,
        "spelling_deduction": spelling_deduction,
        "grammar_deduction": grammar_deduction,
        "readability_deduction": readability_deduction,
        "plagiarism_deduction": plagiarism_deduction
    }

def check_content(request, submission_id):
    submission = get_object_or_404(WritingSubmission, id=submission_id)
    submission.status = 'completed'  # Update status to 'completed' when content checked
    submission.save()

    file_path = submission.file.path
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    results = score_text(content)

    return JsonResponse({'results': results})

def read_file_content(request, submission_id):
    submission = get_object_or_404(WritingSubmission, id=submission_id)
    file_path = submission.file.path
    submission.status = 'opened and under review'  # Make sure 'opened' is a valid choice in your model
    submission.save()
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return render(request, 'display_content.html', {'content': content, 'submission_id': submission_id})

@login_required
def submission_status(request):
    submissions = WritingSubmission.objects.filter(user=request.user)
    return render(request, 'submission_status.html', {'submissions': submissions})


















@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'landing_page.html')

def registration(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        qualification = request.POST.get('qualification')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        state = request.POST.get('state')
        city = request.POST.get('city')

        image = request.FILES.get('image')  # Use get() to handle missing field

        if password != password1:
            return HttpResponse("Your password and confirm password do not match!")

        try:
            usr = User.objects.create_user(
                username=username, email=email, password=password, is_active=1)
            usr.save()
            
            # Check if image is provided, set a default if not
            if not image:
                image = 'default/path/to/default/image.jpg'  # or handle as needed

            par = UserReg.objects.create(
                user=usr, address=address, qualification=qualification,
                phone_number=phone_number, location=location, state=state, city=city, image=image)
            par.save()
            return redirect('login')  # Use named URL
        except Exception as e:
            msg = f'Something went wrong: {str(e)}'  # Provide specific error message
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
                return redirect("admin_master_view")
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
    return redirect("admin_master_view")

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
                file=file,
                status='submitted'  
            )
            submission.save()
            return redirect('home')  
        else:
            return render(request, 'submit_writing.html', {'error': 'All fields are required.'})

    return render(request, 'submit_writing.html')



def admin_master_view(request):
    msg = ''
    data = Master.objects.all()
    return render(request, 'master_view_request.html', {"data": data, "msg": msg})

# def view_submissions(request):
#     msg = ''
#     data = UserReg.objects.all()
#     return render(request, 'review_submissions.html', {"data": data, "msg": msg})

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def view_submissions(request):
    submissions = WritingSubmission.objects.filter(status__in=['submitted', 'opened and under review'])
    return render(request, 'review_submissions.html', {"submissions": submissions})

#accept     
def accept_submission(request, submission_id):
    submission = get_object_or_404(WritingSubmission, id=submission_id)
    submission.status = 'open'  # Update status to 'open' when accepted
    submission.save()
    return redirect('submission_status')


def evaluation_page(request):
    accepted_submissions = WritingSubmission.objects.filter(is_accepted=True)
    return render(request, 'evaluation.html', {'submissions': accepted_submissions})

@login_required
def save_feedback(request, submission_id):
    if request.method == 'POST':
        submission = get_object_or_404(WritingSubmission, id=submission_id)
        
        # Extracting and converting values
        spelling_mark = float(request.POST.get('spelling_mark', 0))
        grammar_mark = float(request.POST.get('grammar_mark', 0))
        plagiarism_mark = request.POST.get('plagiarism_mark', '0').replace('%', '')
        total_mark = float(request.POST.get('total_mark', 0))

        # Convert plagiarism_mark to float
        plagiarism_mark = float(plagiarism_mark)
        
        reviewed_by = request.user.username

        # Create FeedbackDetails instance
        FeedbackDetails.objects.create(
            submission=submission,
            spelling_mark=spelling_mark,
            grammar_mark=grammar_mark,
            plagiarism_mark=plagiarism_mark,
            total_mark=total_mark,
            reviewed_by=reviewed_by
        )
        return redirect('home')  # Change to the appropriate redirect URL

    return redirect('home')


def submission_history(request):
    # Fetch all submissions and prefetch the related feedback details
    submissions = WritingSubmission.objects.prefetch_related('feedbackdetails_set').all()
    
    context = {
        'submissions': submissions,
    }
    
    return render(request, 'submission_history.html', context)

def subm_his_user(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated

    # Fetch submissions related to the logged-in user and prefetch related feedback details
    submissions = WritingSubmission.objects.filter(user=request.user).prefetch_related('feedbackdetails_set')

    context = {
        'submissions': submissions,
    }
    
    return render(request, 'subm_his_user.html', context)



# def read_file_content(request, submission_id):
#     submission = get_object_or_404(WritingSubmission, id=submission_id)
#     file_path = submission.file.path

#     with open(file_path, 'rb') as file:
#         raw_data = file.read()
#         result = chardet.detect(raw_data)
#         encoding = result['encoding']
    
#     try:
#         with open(file_path, 'r', encoding=encoding) as file:
#             file_content = file.read()
#     except UnicodeDecodeError:
#         file_content = "Unable to decode file content."

#     return render(request, 'read_file_content.html', {'submission': submission, 'file_content': file_content})


@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')
