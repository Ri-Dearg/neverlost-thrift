from django.shortcuts import render


def home_page(request):
    """Renders the Homepage as a ist of products."""
    return render(request, 'products/index.html')
