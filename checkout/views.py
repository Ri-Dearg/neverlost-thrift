from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.views.generic.edit import CreateView

from products.models import Product
from .models import Order


class OrderCreateView(CreateView):
    model = Order
    fields = ['full_name', 'email', 'phone_number',
              'street_address1', 'street_address2',
              'town_or_city', 'postcode', 'country',
              'county', ]

    def dispatch(self, *args, **kwargs):
        cart = self.request.session.get('cart', {})
        if not cart:
            messages.error(self.request, "The cart is empty")
            return redirect(reverse('products:list'))
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_dict = self.request.session.get('cart', {})
        cart_list = []
        for key in cart_dict:
            cart_list.append(key)
        products = Product.objects.filter(id__in=cart_list)

        order_form = context['form']

        context['products'] = products
        context['order_form'] = order_form
        return context
