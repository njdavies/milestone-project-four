from django.db import models
from products.models import Product


COUNTRY_CHOICES = [
    ('united kingdom', 'United Kingdom'),
    ('united states', 'United States'),
    ('france', 'France'),
    ('germany', 'Germany'),
]


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(
        max_length=40, blank=False, choices=COUNTRY_CHOICES)
    postcode = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{0} & {1}".format(self.product.name, self.product.buyout_price)
