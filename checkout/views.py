from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.views.generic import CreateView, DetailView
from django.conf import settings


from phonenumber_field import formfields, widgets

from products.models import Product
from .models import Order, OrderLineItem
from cart.context_processors import get_cart

import stripe


class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'


class OrderCreateView(CreateView):
    """Creates an Order on payment completion"""
    model = Order
    fields = ['full_name', 'email', 'phone_number', 'street_address_1',
              'street_address_2', 'town_or_city', 'county',
              'country', 'postcode']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['full_name'].widget.attrs = {'placeholder': 'Full Name'}
        form.fields['email'].widget.attrs = {'placeholder': 'Email Address'}
        form.fields['phone_number'] = formfields.PhoneNumberField(
            label='Phone Number',
            widget=widgets.PhoneNumberPrefixWidget(
                attrs={
                    'type': 'tel',
                    'placeholder': 'xxxxxxxxx',
                    'class': 'custom-select',
                    'pattern': '[0-9]+',
                }),
            initial='+353')
        form.fields['street_address_1'].widget.attrs = {
            'placeholder': 'Street Address 1'}
        form.fields['street_address_2'].widget.attrs = {
            'placeholder': 'Street Address 2'}
        form.fields['town_or_city'].widget.attrs = {
            'placeholder': 'Town or City'}
        form.fields['county'].widget.attrs = {'placeholder': 'County'}
        form.fields['country'].widget.attrs = {'placeholder': 'Country'}
        form.fields['postcode'].widget.attrs = {'placeholder': 'Postcode'}
        return form

    def dispatch(self, *args, **kwargs):
        """Checks for items in cart and redirects to the home page if there
        aren't any."""
        cart = self.request.session.get('cart', {})
        if not cart:
            messages.warning(self.request, "The cart is empty.")
            return redirect(reverse('products:product-list'))
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        order = form.save()
        cart = self.request.session.get('cart', {})
        for item_id, item_data in cart.items():
            try:
                product = Product.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=item_data,
                )
                order_line_item.save()
            except Product.DoesNotExist:
                messages.error(self.request, (
                    "One of the products in your cart wasn't found in our collection. \
                    Please call us for assistance!")
                )
                order.delete()

        self.request.session['save_info'] = 'save-info' in self.request.POST

        if 'cart' in self.request.session:
            del self.request.session['cart']

        if self.request.user.is_authenticated:
            order.user_profile = self.request.user.userprofile
            order.save()
        messages.success(self.request, f'Order successfully processed! \
            Your order number is {order.order_number}. A confirmation \
            email will be sent to {order.email}.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'There was a problem processing the order. Please double check your information.') # noqa E501
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context"""
        context = super().get_context_data(**kwargs)
        # Details necessary for Stripe payment processing
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart_contents = get_cart(self.request)
        total = cart_contents['cart_total']

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Gets the Product IDs from the cart, places them in a list and then
        # filters the list for display.
        cart_dict = self.request.session.get('cart', {})
        cart_list = []
        for key in cart_dict:
            cart_list.append(key)
        products = Product.objects.filter(id__in=cart_list)

        order_form = context['form']

        context['stripe_public_key'] = stripe_public_key
        context['client_secret'] = intent.client_secret
        context['products'] = products
        context['order_form'] = order_form
        return context
