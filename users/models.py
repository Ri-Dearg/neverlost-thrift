from django.db import models
from django.contrib.auth.models import User


from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from products.models import Product


class UserProfile(models.Model):
    """User Profile used to store default delivery information and
    liked/bookmarked items"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_name = models.CharField(max_length=50,
                                    default='', blank=True)
    default_phone_number = PhoneNumberField(default='', blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               default='', blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               default='', blank=True)
    default_city = models.CharField(max_length=40,
                                    default='', blank=True)
    default_county = models.CharField(max_length=80,
                                      default='', blank=True)
    default_postcode = models.CharField(max_length=20,
                                        default='', blank=True)
    default_country = CountryField(blank_label='Country',
                                   default='', blank=True)
    liked_products = models.ManyToManyField(Product, blank=True,
                                            related_name='users')

    def __str__(self):
        return self.user.username
