from django.test import TestCase
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
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)