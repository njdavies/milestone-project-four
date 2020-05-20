from django.test import TestCase
from django.urls import reverse


class SearchPageViewTest(TestCase):
    """
    Tests to check that the Search page exists at the 
    correct URL, uses the correct view and uses the correct template
    """

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/search/')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_name(self):
        resp = self.client.get(reverse('search'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'products-search.html')
