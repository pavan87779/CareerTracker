from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):

    STATUS_CHOICES = [

        ('Applied', 'Applied'),

        ('OA Scheduled', 'OA Scheduled'),

        ('Interview Scheduled', 'Interview Scheduled'),

        ('HR Round', 'HR Round'),

        ('Rejected', 'Rejected'),

        ('Offer Received', 'Offer Received'),

        ('Joined', 'Joined'),

    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(max_length=200)

    role = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    salary = models.CharField(
        max_length=100,
        blank=True
    )

    application_date = models.DateField()

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    recruiter_name = models.CharField(
        max_length=200,
        blank=True
    )

    recruiter_email = models.EmailField(
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.company_name} - {self.role}"
    



class InterviewNote(models.Model):

    ROUND_CHOICES = [

        ('HR Round', 'HR Round'),

        ('Technical Round', 'Technical Round'),

        ('Managerial Round', 'Managerial Round'),

        ('Final Round', 'Final Round'),

    ]

    job_application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE
    )

    round_type = models.CharField(
        max_length=100,
        choices=ROUND_CHOICES
    )

    questions = models.TextField()

    feedback = models.TextField(
        blank=True
    )

    preparation_notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.job_application.company_name} - {self.round_type}"