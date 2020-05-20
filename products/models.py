from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    era = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    created_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    starting_price = models.DecimalField(
        null=True, decimal_places=2, max_digits=8)
    buyout_price = models.DecimalField(
        null=True, decimal_places=2, max_digits=8)
    status = models.CharField(max_length=6, null=False)

    def __str__(self):
        return self.name


class Bid(models.Model):
    name = models.CharField(max_length=100, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    current_bid = models.DecimalField(
        null=True, decimal_places=2, max_digits=8)
    current_bid_user = models.CharField(max_length=100, null=True)
    current_bid_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
