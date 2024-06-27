from django.db import models
from django.contrib.auth.models import User

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

    # New fields
    plagiarism_mark = models.IntegerField(default=0)
    grammatical_mark = models.IntegerField(default=0)
    master_check_mark = models.IntegerField(default=0)
    total_mark = models.IntegerField(default=0)
    reviewed_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
