from django.contrib import admin
from .models import (
    JobApplication,
    InterviewNote
)

admin.site.register(JobApplication)
admin.site.register(InterviewNote)