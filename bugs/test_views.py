from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Bug


class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_get_bug_list_page(self):
        page = self.client.get("/bugs")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs_list.html")
        
    def test_get_add_a_bug_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_a_bug.html")
        
    def test_get_edit_bug_page(self):
        bug = Bug(title = 'Create a Test', description = 'This creates a new test')
        bug.save()
        page = self.client.get("/edit/{0}".format(bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_a_bug.html")
        
    def test_get_edit_page_for_bug_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        
    def test_post_create_a_bug(self):
        response = self.client.post("/add", {'title': 'Create a Test', 'description': 'This creates a test'})
        bug = get_object_or_404(Bug, pk=1)
        self.assertEqual(bug.ticket_status, 'Todo')
        
    #def test_post_edit_an_item(self):
     #   bug = Bug(title = "Create an Test", desription = "This creates a test")
      #  bug.save()
       # id = bug.id
        #response = self.client.post("/edit/{0}".format(id), {"title": "A different title"})
    #    bug = get_object_or_404(Bug, pk=id)
        
     #   self.assertEqual("A different title", bug.title)