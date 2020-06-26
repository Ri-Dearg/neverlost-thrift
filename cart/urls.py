from django.urls import path
from .views import add_to_cart, remove_from_cart, CartListView

urlpatterns = [
    path('', CartListView.as_view(), name='cart-list'),
    path('add/<int:item_id>/', add_to_cart, name='add-to-cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove-from-cart')
]
