from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import WritingSubmission

class WritingSubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'submitted_at')
    search_fields = ('title', 'category', 'user__username')

admin.site.register(WritingSubmission, WritingSubmissionAdmin)
