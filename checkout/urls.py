from django.urls import path
from .views import OrderCreateView, OrderDetailView, OrderListView, cache_data
from .webhooks import webhook

urlpatterns = [
    path('', OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/',
         OrderDetailView.as_view(), name='order-detail'),
    path('orders/',
         OrderListView.as_view(), name='order-list'),
    path('cache_data/', cache_data, name='cache-data'),
    path('webhook/', webhook, name='webhook'),
]
