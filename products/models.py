from django.db import models
from django.utils import timezone
from django.contrib.postgres import fields


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    date_added = models.DateTimeField(default=timezone.now)
    admin_tags = fields.ArrayField(models.CharField(max_length=40), size=7)
    user_tags = fields.ArrayField(models.CharField(max_length=40),
                                  size=7,
                                  default=list)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.name}, {self.price}'
