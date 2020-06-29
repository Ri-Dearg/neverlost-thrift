from django.urls import path
from .views import cart_toggle, CartListView

urlpatterns = [
    path('', CartListView.as_view(), name='cart-list'),
    path('ajax/toggle/', cart_toggle, name='cart-toggle'),
]
