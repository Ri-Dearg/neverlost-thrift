from django.urls import path
from .views import cart_toggle, update_cart, CartListView

urlpatterns = [
    path('', CartListView.as_view(), name='cart-list'),
    path('ajax/toggle/', cart_toggle, name='cart-toggle'),
    path('update/', update_cart, name='cart-update'),
]
