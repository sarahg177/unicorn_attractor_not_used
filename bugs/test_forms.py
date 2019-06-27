from django.test import TestCase
from .forms import BugForm

# Create your tests here.
class TestBugsBugForm(TestCase):
    
    def test_cannot_create_an_item_with_just_title_and_description(self):
        form = BugForm({'title': 'Create Tests', 'description': 'This creates tests'})
        self.assertFalse(form.is_valid())
        
    def test_correct_message_for_missing_field(self):
        form = BugForm({'title': '', 'description': 'This creates test', 'issue_type': 'Feature', 'ticket_status': 'Todo'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors ['title'], [u'This field is required.'] )