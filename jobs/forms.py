from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:

        model = JobApplication

        fields = [
            'company_name',
            'role',
            'location',
            'salary',
            'application_date',
            'status',
            'recruiter_name',
            'recruiter_email',
            'notes',
        ]

        widgets = {

            'application_date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'notes': forms.Textarea(
                attrs={'rows': 4}
            ),
        }