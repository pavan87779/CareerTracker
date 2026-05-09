from django import forms
from .models import InterviewNote


class InterviewNoteForm(forms.ModelForm):

    class Meta:

        model = InterviewNote

        fields = [

            'round_type',
            'questions',
            'feedback',
            'preparation_notes',
        ]

        widgets = {

            'questions': forms.Textarea(
                attrs={'rows': 4}
            ),

            'feedback': forms.Textarea(
                attrs={'rows': 3}
            ),

            'preparation_notes': forms.Textarea(
                attrs={'rows': 4}
            ),
        }