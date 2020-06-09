import sys

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone
from django.contrib.postgres import fields

from PIL import Image
from io import BytesIO


class Category(models.Model):
    """Defines categories to be used with products."""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    """Defines the Product Class."""
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default='default.png',
                              upload_to='product_images')
    date_added = models.DateTimeField(default=timezone.now)
    admin_tags = fields.ArrayField(models.CharField(max_length=40), size=4)
    user_tags = fields.ArrayField(models.CharField(max_length=40),
                                  size=4,
                                  default=list, blank=True)

    def save(self, *args, **kwargs):
        """Image resizing, snippet repurposed from:
        https://djangosnippets.org/snippets/10597/ """
        # Opening the image
        this_object = None
        try:
            this_object = Product.objects.get(pk=self.id)
        except Product.DoesNotExist:
            pass
        finally:
            img = Image.open(self.image)
            img_format = img.format.lower()

            # Prevents images from being copied on every save
            # will save a new copy on an upload
            if (this_object and self.image.name != this_object.image.name) \
                    or (not this_object):
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
                    'image/jpeg', sys.getsizeof(output),
                    None)

                super().save(*args, **kwargs)
            else:
                super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.name}: €{self.price}'
