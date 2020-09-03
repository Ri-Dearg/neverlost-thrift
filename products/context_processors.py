from .models import StockDrop, Category


def get_stockdrops(request):
    """Provides stockdrop info for the navbar on all pages."""
    stockdrops = StockDrop.objects.filter(display=True)
    return {'stockdrops': stockdrops}


def get_categories(request):
    """Provides category info for the navbar on all pages"""
    categories = Category.objects.all().order_by('name')
    return {'categories': categories}
