from django.urls import path
from .views import OrderCreateView, OrderDetailView, OrderListView

urlpatterns = [
    path('', OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/',
         OrderDetailView.as_view(), name='order-detail'),
    path('orders/',
         OrderListView.as_view(), name='order-list'),
]
