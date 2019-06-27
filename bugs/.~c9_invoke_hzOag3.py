from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'issue_type', 'description', 'ticket_status')