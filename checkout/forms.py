from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Build the checkout form based on CI video Course:
    Project - Boutique Ado  The Checkout App  Views & Templates Part 1
    """

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )
