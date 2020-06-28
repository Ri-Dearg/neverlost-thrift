import uuid

from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from users.models import UserProfile
from products.models import Product


class Order(models.Model):
    """Model that sets the fields for orders"""
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, default='', blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address_1 = models.CharField(max_length=80, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, default='', blank=True)
    county = models.CharField(max_length=80, default='', blank=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def get_absolute_url(self):
        return reverse('checkout:order-detail', args=[str(self.id)])

    def _update_total(self):
        """Updates the grand total figure in an order."""
        self.order_total = self.lineitems.aggregate(Sum(
            'lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total

    def _generate_order_number(self):
        """Generates a random order number"""
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """Saves the order number"""
        self._update_total()
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """Associates the product to the order with quantity and total cost"""
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              null=False, blank=False,
                              related_name='lineitems')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         editable=False,
                                         null=False, blank=False)

    def save(self, *args, **kwargs):
        """Saves the total cost"""
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
