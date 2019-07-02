from django import forms
from .models import Bug, Comments

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('issue_type', 'title', 'description')
        
class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': '10', 'cols': '5'})
    )

    class Meta:
        model = Comments
        fields = ['comment']