from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    """Renders the home page with a Products List."""
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_active = True
        context['product_active'] = product_active
        return context


class ProductDetailView(DetailView):
    """Renders the product detail page"""
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_active = True
        context['categories_active'] = categories_active
        return context
