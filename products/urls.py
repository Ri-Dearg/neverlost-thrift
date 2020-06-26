from django.urls import path
from .views import (CategoryDetailView,
                    ProductListView,
                    ProductDetailView,
                    StockDropDetailView)

urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('category/<int:pk>/',
         CategoryDetailView.as_view(),
         name="category-detail"),
    path('product/<int:pk>/',
         ProductDetailView.as_view(), name='product-detail'),
    path('stockdrop/<int:pk>/',
         StockDropDetailView.as_view(),
         name="stockdrop-detail"),
]
