from django.views.generic import ListView, DetailView
from .models import Product, StockDrop


class ProductListView(ListView):
    """Renders the home page with a Products List."""
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stock_drops = StockDrop.objects.filter(display=True)
        products_active = True

        context['stockdrops'] = stock_drops
        context['products_active'] = products_active
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


class StockDropDetailView(DetailView):
    """Renders the home page with a Products List."""
    model = StockDrop
    context_object_name = 'stockdrop'
