from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import (SearchQuery,
                                            SearchRank,
                                            SearchVector)

from .models import Category, Product, StockDrop


class ProductListView(ListView):
    """Renders the home page with a Products List.
    If there is a GET request, performs a search."""
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        """Returns either all Products or a query appropriately."""
        if 'query' in self.request.GET:
            # Returns all products if there's no query
            if self.request.GET['query'] == '':
                messages.warning(self.request,
                                 "You didn't search for anything")
                return Product.objects.all().order_by('-stock', '-popularity')
            else:
                # Performs a full text search using Postgres database
                # functionality, weighting tags above other text
                self.user_query = self.request.GET['query']
                self.vector = SearchVector(
                    'name',
                    'description',
                    'category',
                    weight='B') + SearchVector(
                        'admin_tags', weight='A')
                self.query = SearchQuery(self.user_query)
                self.rank = SearchRank(self.vector, self.query)

                return Product.objects.annotate(
                    rank=self.rank).order_by(
                    '-rank').filter(rank__gt=0)
        else:
            return Product.objects.all().order_by('-stock', '-popularity')

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        # Selects the active tab
        if 'query' not in self.request.GET and self.request.path == '/':
            all_products_active = True
            context['all_products_active'] = all_products_active

        products = context['products']
        paginator = Paginator(products, 9)
        page_number = self.request.GET.get('page')

        if 'query' in self.request.GET:
            if 'page' in self.request.GET['query']:
                page_number = self.request.GET['query'].rpartition('=')[-1]
            keyword = self.request.GET['query'].split('?')[0]
            context['keyword'] = keyword

        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj

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

        selected_product = context['product']
        selected_category = selected_product.category
        products = Product.objects.exclude(
            pk=selected_product.id).filter(
                category=selected_category).order_by(
                    '-stock', '-popularity')[:9]

        context['categories_active'] = categories_active
        context['products'] = products
        return context


class StockDropDetailView(DetailView):
    """Renders the home page with a Products List."""
    model = StockDrop
    context_object_name = 'stockdrop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = context['stockdrop'].products.all().order_by(
            '-stock', '-popularity')
        paginator = Paginator(products, 9)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        key = self.request.path.split('/')[2]

        # Selects the active tab
        stockdrops_active = True

        context['page_obj'] = page_obj
        context['stockdrops_active'] = stockdrops_active
        context['collection_active'] = key
        return context


class CategoryDetailView(DetailView):
    """Renders the home page with a Products List."""
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = context['category'].products.all().order_by(
            '-stock', '-popularity')
        paginator = Paginator(products, 9)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        key = self.request.path.split('/')[2]

        # Selects the active tab
        categories_active = True

        context['page_obj'] = page_obj
        context['categories_active'] = categories_active
        context['collection_active'] = key
        return context
