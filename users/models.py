from django.db import models
from django.contrib.auth.models import User


from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from products.models import Product


class UserProfile(models.Model):
    """User Profile used to store default delivery information and
    liked/bookmarked items"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_shipping_name = models.CharField(max_length=50,
                                             default='', blank=True)
    default_shipping_phone_number = PhoneNumberField(default='', blank=True)
    default_shipping_street_address_1 = models.CharField(max_length=80,
                                                         default='',
                                                         blank=True)
    default_shipping_street_address_2 = models.CharField(max_length=80,
                                                         default='',
                                                         blank=True)
    default_shipping_city = models.CharField(max_length=40,
                                             default='', blank=True)
    default_shipping_county = models.CharField(max_length=80,
                                               default='', blank=True)
    default_shipping_postcode = models.CharField(max_length=20,
                                                 default='', blank=True)
    default_shipping_country = CountryField(blank_label='Country',
                                            default='', blank=True)
    default_billing_name = models.CharField(max_length=50,
                                            default='', blank=True)
    default_billing_phone_number = PhoneNumberField(default='', blank=True)
    default_billing_street_address_1 = models.CharField(max_length=80,
                                                        default='', blank=True)
    default_billing_street_address_2 = models.CharField(max_length=80,
                                                        default='', blank=True)
    default_billing_city = models.CharField(max_length=40,
                                            default='', blank=True)
    default_billing_county = models.CharField(max_length=80,
                                              default='', blank=True)
    default_billing_postcode = models.CharField(max_length=20,
                                                default='', blank=True)
    default_billing_country = CountryField(blank_label='Country',
                                           default='', blank=True)

    liked_products = models.ManyToManyField(Product, blank=True,
                                            related_name='users',
                                            through='Liked')

    def _readable_field(self, *args, **kwargs):
        """Alters the field names to make them user friendly"""
        fields = self._meta.fields
        readable_names = []
        values = []

        for field in range(2, 18):
            field_object = fields[field]
            name = field_object.name.replace('_', ' ')
            readable_names.append(name)

            value = field_object.value_from_object(self)
            values.append(value)

        return readable_names, values

    def __str__(self):
        return self.user.username


class Liked(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.product}, {self.atetime_added}'
