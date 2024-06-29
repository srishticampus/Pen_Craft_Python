from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserReg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Profile', default='profile/default.jpg')
    qualification = models.CharField(max_length=100,default='Not Provided')
    phone_number = models.CharField(max_length=20,default='Not Provided')
    address = models.CharField(max_length=255,default='Not Provided')
    location = models.CharField(max_length=100,default='Not Provided')
    state = models.CharField(max_length=100,default='Not Provided')
    city = models.CharField(max_length=100,default='Not Provided')

    def __str__(self):
        return self.user.username
    

class Master(models.Model):
    username = models.CharField(max_length=150,default='name')  # Adjust max_length according to your needs
    email = models.EmailField(default='example@example.com')
    phone = models.CharField(max_length=50, default='Not Provided')
    address = models.CharField(max_length=255, default='Not Provided')
    qual = models.CharField(max_length=100, default='Not Provided')  # Adjust max_length according to your needs
    field = models.CharField(max_length=100, default='Default Value')  # Adjust max_length according to your needs
    img = models.ImageField(upload_to='Profile')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class WritingSubmission(models.Model):
    CATEGORY_CHOICES = [
        ('Literature-Story', 'Literature-Story'),
        ('Poem', 'Poem'),
        ('Novel', 'Novel'),
        ('Article', 'Article'),
        ('Journals', 'Journals'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)



    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('open', 'Open'),
        ('completed', 'Completed'),
    )


    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class FeedbackDetails(models.Model):
    submission = models.ForeignKey(WritingSubmission, on_delete=models.CASCADE)
    spelling_mark = models.FloatField(default=0)  # Changed to FloatField
    plagiarism_mark = models.FloatField(default=0)  # Changed to FloatField
    grammar_mark = models.FloatField(default=0)  # Changed to FloatField
    total_mark = models.FloatField(default=0)  # Changed to FloatField
    reviewed_by = models.CharField(max_length=150, default='') 

    def __str__(self):
        return self.submission.title