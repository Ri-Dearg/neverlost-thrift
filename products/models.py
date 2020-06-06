from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils import timezone
from django.contrib.postgres import fields


class Product(models.Model):
    """Defines the Product Class."""
    name = models.CharField(max_length=254, default='')
    blurb = models.CharField(max_length=50, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default='default.png',
                              upload_to='product_images')
    date_added = models.DateTimeField(default=timezone.now)
    admin_tags = fields.ArrayField(models.CharField(max_length=40), size=7)
    user_tags = fields.ArrayField(models.CharField(max_length=40),
                                  size=7,
                                  default=list, blank=True)

    def save(self, *args, **kwargs):
        """Image resizing, snippet repurposed from:
        https://djangosnippets.org/snippets/10597/ """
        # Opening the image
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
            'image/jpeg', sys.getsizeof(output),
            None)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.name}: €{self.price}'
