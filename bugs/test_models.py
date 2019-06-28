from django.test import TestCase
from .models import Bug

class TestBugModel(TestCase):
    def test_issue_type_defaults_to_Feature(self):
        bug = Bug(title = "Create a Test")
        bug.save()
        self.assertEqual(bug.title, "Create a Test")
        self.assertEqual(bug.issue_type, 'Feature')
        
    def test_ticket_status_defaults_to_Todo(self):
        bug = Bug(title = "Create a Test")
        bug.save()
        self.assertEqual(bug.title, "Create a Test")
        self.assertEqual(bug.ticket_status, 'Todo')
        
    def test_can_creaate_a_bug_with_a_title_and_issue_type_of_Bug(self):
        bug = Bug(title = "Create a Test", issue_type = "Bug")
        bug.save()
        self.assertEqual(bug.title, "Create a Test")
        self.assertEqual(bug.issue_type, 'Bug')