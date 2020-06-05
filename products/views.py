from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    """Renders the home page with a Products List."""
    model = Product
    context_object_name = 'products'
