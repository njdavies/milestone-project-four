from django import forms
from django.forms import ModelForm
from .models import Product, Bid


class BidForm(ModelForm):

    current_bid = forms.DecimalField(
        label=False)

    class Meta:
        model = Bid
        fields = ['current_bid', ]
