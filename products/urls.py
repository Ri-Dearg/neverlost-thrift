from django.urls import path
from .views import ProductListView, ProductDetailView, StockDropDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('product/<int:pk>/',
         ProductDetailView.as_view(), name='product-detail'),
    path('stockdrop/<int:pk>/',
         StockDropDetailView.as_view(),
         name="stockdrop-detail"),
]
