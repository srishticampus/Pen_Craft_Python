from django import forms
from .models import WritingSubmission

class WritingSubmissionForm(forms.ModelForm):
    class Meta:
        model = WritingSubmission
        fields = ['category', 'title', 'description', 'file']
