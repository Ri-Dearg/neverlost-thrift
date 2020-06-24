from django.shortcuts import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import (SearchQuery,
                                            SearchRank,
                                            SearchVector)

from .models import Product, StockDrop


class ProductListView(ListView):
    """Renders the home page with a Products List.
    If there is a GET request, performs a search."""
    model = Product
    context_object_name = 'products'
    ordering = ['-date_added']

    def get_queryset(self):
        """Returns either all Products or a query appropriately."""
        if 'query' in self.request.GET:
            # Returns all products if there's no query
            if self.request.GET['query'] == '':
                messages.warning(self.request,
                                 "You didn't search for anything")
                return Product.objects.all()

            # Performs a full text search using Postgres database
            # functionality, weighting tags above other text
            self.user_query = self.request.GET['query']
            self.vector = SearchVector('name', 'description', weight='A') + \
                SearchVector('admin_tags', 'user_tags', weight='B')
            self.query = SearchQuery(self.user_query)
            self.rank = SearchRank(self.vector, self.query)

            return Product.objects.annotate(rank=self.rank).order_by('-rank')\
                .filter(rank__gt=0)

        return Product.objects.all()

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        # Displays stockdrops if there is no query
        if not self.request.GET:
            stockdrops = StockDrop.objects.filter(display=True)
            context['stockdrops'] = stockdrops

        # Selects the active tab
        products_active = True

        context['products_active'] = products_active
        return context


class ProductDetailView(DetailView):
    """Renders the product detail page"""
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        # Selects the active tab       
        categories_active = True

        context['categories_active'] = categories_active
        return context


class StockDropDetailView(DetailView):
    """Renders the home page with a Products List."""
    model = StockDrop
    context_object_name = 'stockdrop'
