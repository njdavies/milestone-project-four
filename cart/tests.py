from django.test import TestCase
from django.urls import reverse


class CartPageTests(TestCase):
    """
    Tests to check that the cart page exists and returns an HTTP 200 status code, 
    uses the correct url name in the view and uses the correct template
    """

    def test_cart_page_status_code(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
