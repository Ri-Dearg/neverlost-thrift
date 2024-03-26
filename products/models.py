import contextlib
import sys
from io import BytesIO

from django.contrib.postgres import fields
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils import timezone
from PIL import Image

from config import settings


class Category(models.Model):
    """Defines categories to apply to products.
    A simple model to group products."""

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Defines the Product Class. Many fields are optional.
    A default image is uploaded if no image is selected.
    Images will be resized on upload to 500x500px square shape.
    I would recommend cropping your images to a 1:1 ratio first.
    It automatically sets stock values based on is_uniqe value.
    Generates the 'popuarity' value on save.This value is a combination of the
    total quantity an item was sold and how many unique users have liked it."""

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='products',
    )
    stock_drop = models.ForeignKey(
        'StockDrop',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='products',
    )

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    size = models.CharField(max_length=2, default='', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(
        default=f'{settings.BUCKET_NAME}/default.png',
        upload_to='product_images',
    )
    date_added = models.DateTimeField(default=timezone.now)
    admin_tags = fields.ArrayField(models.CharField(max_length=40), size=8)
    is_unique = models.BooleanField(default=True, blank=False, null=False)
    stock = models.SmallIntegerField(default=1, blank=False, null=False)
    times_purchased = models.IntegerField(
        default=0, blank=False, null=False, editable=False
    )
    popularity = models.IntegerField(
        default=0, blank=False, null=False, editable=False
    )

    class Meta:
        ordering = ['-popularity']

    def __str__(self):
        return f'{self.name}: €{self.price}'

    def save(self, *args, **kwargs):
        """Generates default stock values.
        Will restock items that are not unique.
        Updates the 'popularity' value.
        Image resizing, snippet repurposed from:
        https://djangosnippets.org/snippets/10597/"""

        # Declares a check to see if the product exists.
        this_object = None
        try:
            this_object = Product.objects.get(pk=self.id)
        except Product.DoesNotExist:
            pass
        finally:
            # Updates popularity (See below)
            self._update_popularity(self, *args, **kwargs)

            # Sets default stock to 50 and/or restocks non-unique items
            if not self.is_unique and self.stock == 1:
                self.stock = 50

            # Prevents images from being copied on every save
            # will save a new copy on an upload
            if (
                (this_object and self.image.name != this_object.image.name)
                or (not this_object)
                and (self.image.name != f'{settings.BUCKET_NAME}/default.png')
            ):
                # opens the image before it is saved.
                img = Image.open(self.image)
                img_format = img.format.lower()

                # Image is resized
                output_size = (500, 500)
                img = img.resize(size=(output_size))

                # Converts format while in memory
                output = BytesIO()
                img.save(output, format=img_format)
                output.seek(0)

                # Replaces the Imagefield value with the newly converted image
                self.image = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    f'{self.image.name.split(".")[0]}.{img_format}',
                    'image/jpeg',
                    sys.getsizeof(output),
                    None,
                )
                super().save(*args, **kwargs)
            else:
                super().save(*args, **kwargs)

    def _update_popularity(self, *args, **kwargs):
        """Used for item ordering so more popular items are displayed first.
        A combination of total unique likes and number sold."""
        with contextlib.suppress(ValueError):
            self.popularity = self.users.count() + self.times_purchased


class StockDrop(models.Model):
    """Allows for the creation of a collection of Products.
    You can add a splash image which will be resized and a blurb.
    Images will be resized on upload to 1289x480px square shape.
    I would recommend cropping your images to a 8:3 ratio first."""

    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='stock_drop')
    date_added = models.DateTimeField(default=timezone.now)
    display = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """Image resizing, snippet repurposed from:
        https://djangosnippets.org/snippets/10597/"""
        # Opening the image
        this_object = None
        try:
            this_object = StockDrop.objects.get(pk=self.id)
        except StockDrop.DoesNotExist:
            pass
        finally:
            # Prevents images from being copied on every save
            # will save a new copy on an upload
            if (this_object and self.image.name != this_object.image.name) or (
                not this_object
            ):
                img = Image.open(self.image)
                img_format = img.format.lower()
                # Image is resized
                output_size = (1280, 480)
                img = img.resize(size=(output_size))

                # Converts format while in memory
                output = BytesIO()
                img.save(output, format=img_format)
                output.seek(0)

                # Replaces the Imagefield value with the newly converted image
                self.image = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    f'{self.image.name.split(".")[0]}.{img_format}',
                    'image/jpeg',
                    sys.getsizeof(output),
                    None,
                )

                super().save(*args, **kwargs)
            else:
                super().save(*args, **kwargs)

    class Meta:
        """Orders by the most recent created by default."""

        ordering = ['-date_added']

    def __str__(self):
        return f'{self.date_added.strftime("%B")}: {self.name}'
