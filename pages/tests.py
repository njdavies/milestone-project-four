from django.test import SimpleTestCase
from django.urls import reverse

"""
Tests to check that each of the three static pages exist at the 
correct URL, use the correct view and use the correct template
"""


class HomePageViewTest(SimpleTestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')


class AboutPageViewTest(SimpleTestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_name(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'about.html')


class ContactPageViewTest(SimpleTestCase):
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_name(self):
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contact.html')
