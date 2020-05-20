from django.test import TestCase
from django.urls import reverse
from .models import Product, Bid


class ProductsPageTests(TestCase):
    """
    Tests to check that the Products page exists and returns an HTTP 200 status code,
    uses the correct url name in the view and uses the correct template.
    """

    def test_products_page_status_code(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')


class ArtifactPageTests(TestCase):
    """
    Tests to check that the Artifact page exists and uses the correct url name
    in the view and uses the correct template.
    """

    def setUp(self):
        myProduct = Product.objects.create(name='myArtifact')

    def test_artifact_page_status_code(self):
        response = self.client.get('/products/artifact/1')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/products/artifact/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artifact.html')


class BidTests(TestCase):
    """
    Tests to check that when a bid is made this is stored in the database
    and is matched against the correct product
    """

    def setUp(self):
        myProduct = Product.objects.create(name='myArtifact')
        Bid.objects.create(product=myProduct,
                           name=myProduct.name,
                           current_bid=1000)

    def test_bid(self):
        new_product = Product.objects.get(id=1)
        new_bid = Bid.objects.get(id=1)
        self.assertEqual(new_bid.name, new_product.name)
        self.assertEqual(new_bid.current_bid, 1000)
