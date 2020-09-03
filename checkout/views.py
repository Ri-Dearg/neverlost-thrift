from django.shortcuts import redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import CharField, model_to_dict
from django.conf import settings

from phonenumber_field import widgets

from products.models import Product
from .models import Order, OrderLineItem
from cart.context_processors import get_cart

import stripe
import json
import itertools


class OrderDetailView(DetailView):
    """Displays the details for an Order object.
    It doesn't require login as Anonymous users must utilise the view. However,
    it will check if the current user is the user who made the order.
    If an anonymous user has made an order, they should have their order ID
    stored in their session and can access the order that way."""

    model = Order
    context_object_name = 'order'

    def dispatch(self, *args, **kwargs):
        """Checks to make sure that the user trying to access the page is the
        same user that has made the order before the page is accessed."""

        # Gets the user and the Order object
        user = self.request.user
        self.object = self.get_object()

        # Checks to see whether the user is logged in or has the
        # necessary session cookie. If not, they are redirected.
        if user.is_authenticated:
            userprofile = self.request.user.userprofile
            # Checks to see if the user has made this order, else redirects:
            if self.object.user_profile == userprofile:
                return super().dispatch(*args, **kwargs)
            else:
                return redirect(reverse('products:product-list'))
        elif 'my_order' in self.request.session:
            # Checks to see if the user has the correct order in the session:
            if self.request.session['my_order'] == self.object.id:
                return super().dispatch(*args, **kwargs)
            else:
                return redirect(reverse('products:product-list'))
        else:
            return redirect(reverse('products:product-list'))


class OrderListView(LoginRequiredMixin, ListView):
    """Displays all Orders made by a user in reverse chronological order.
    It requires login as anonymous users can't access
    more than one order at a time."""

    model = Order
    context_object_name = 'orders'
    ordering = ['-date']

    def get_queryset(self):
        """Filters the Order to those made only by this user."""
        userprofile = self.request.user.userprofile
        return Order.objects.filter(user_profile=userprofile).order_by('-date')


class OrderCreateView(CreateView):
    """Creates an Order on payment completion.
    Uses custom form widgets and layouts."""

    model = Order
    fields = ['email', 'billing_full_name', 'billing_phone_number',
              'billing_street_address_1', 'billing_street_address_2',
              'billing_town_or_city', 'billing_county',
              'billing_country', 'billing_postcode', 'shipping_full_name',
              'shipping_phone_number', 'shipping_street_address_1',
              'shipping_street_address_2', 'shipping_town_or_city',
              'shipping_county', 'shipping_country', 'shipping_postcode']

    def get_form(self, form_class=None):
        """Adds custom placeholders and widgets to the form"""
        form = super().get_form(form_class)
        form.fields['email'].widget.attrs = {'placeholder': 'Email Address'}
        form.fields['shipping_full_name'].widget.attrs = {'placeholder': 'Full Name'}  # noqa E501
        form.fields['shipping_full_name'].label = 'Full Name'
        form.fields['shipping_phone_number'] = CharField(
            widget=widgets.PhoneNumberPrefixWidget(
                attrs={
                    'type': 'tel',
                    'placeholder': 'Phone Number',
                    'class': 'form-control',
                    'pattern': '[0-9]+',
                }),
            initial='+353')
        form.fields['shipping_street_address_1'].widget.attrs = {
            'placeholder': '123 Main St.'}
        form.fields['shipping_street_address_1'].label = 'Street Address 1'
        form.fields['shipping_street_address_2'].widget.attrs = {
            'placeholder': 'Street Address 2'}
        form.fields['shipping_street_address_2'].label = 'Street Address 2'
        form.fields['shipping_town_or_city'].widget.attrs = {
            'placeholder': 'Town or City'}
        form.fields['shipping_town_or_city'].label = 'City or Town'
        form.fields['shipping_county'].widget.attrs = {
            'placeholder': 'Locality'}
        form.fields['shipping_county'].label = 'County, State or Locality'
        form.fields['shipping_country'].widget.attrs = {'placeholder': 'Country',  # noqa E501
                                                        'class': 'form-control'}  # noqa E501
        form.fields['shipping_country'].label = 'Country'
        form.fields['shipping_postcode'].widget.attrs = {
            'placeholder': 'Postcode'}
        form.fields['shipping_postcode'].label = 'Postcode'
        form.fields['billing_full_name'].widget.attrs = {
            'placeholder': 'Full Name', 'class': 'billing-field'}
        form.fields['billing_full_name'].label = 'Full Name'
        form.fields['billing_phone_number'] = CharField(
            label='Phone Number',
            widget=widgets.PhoneNumberPrefixWidget(
                attrs={
                    'type': 'tel',
                    'placeholder': 'Phone Number',
                    'class': 'form-control billing-field',
                    'pattern': '[0-9]+',
                }),
            initial='+353')
        form.fields['billing_street_address_1'].widget.attrs = {
            'Placeholder': 'Street Address 1', 'class': 'billing-field'}
        form.fields['billing_street_address_1'].label = 'Street Address 1'
        form.fields['billing_street_address_2'].widget.attrs = {
            'placeholder': 'Street Address 2'}
        form.fields['billing_street_address_2'].label = 'Street Address 2'
        form.fields['billing_town_or_city'].widget.attrs = {
            'placeholder': 'Town or City', 'class': 'billing-field'}
        form.fields['billing_town_or_city'].label = 'City or Town'
        form.fields['billing_county'].widget.attrs = {
            'placeholder': 'Locality'}
        form.fields['billing_county'].label = 'County, State or Locality'
        form.fields['billing_country'].widget.attrs = {'placeholder': 'Country',  # noqa E501
                                                       'class': 'form-control billing-field'}  # noqa E501
        form.fields['billing_county'].label = 'Country'
        form.fields['billing_postcode'].widget.attrs = {
            'placeholder': 'Postcode'}
        form.fields['billing_postcode'].label = 'Postcode'
        return form

    def dispatch(self, *args, **kwargs):
        """Checks for items in cart and redirects to the home page if there
        aren't any."""

        cart = self.request.session.get('cart', {})
        if not cart:
            messages.info(self.request, "The cart is empty.")
            return redirect(reverse('products:product-list'))
        return super().dispatch(*args, **kwargs)

    def get_initial(self):
        """If the user is logged in, it sets the initial form values
        to the values in their user profile."""

        initial = super().get_initial()
        if self.request.user.is_authenticated:
            # Gets the UserProfile and makes it a dictionary
            user = self.request.user
            userprofile = user.userprofile
            userprofile_dict = model_to_dict(userprofile)

            # Iterates the fields, sets the email separately, and fills others.
            for field, key in itertools.product(self.fields, userprofile_dict):
                if field == 'email':
                    initial['email'] = user.email
                elif field == key:
                    initial[f'{field}'] = userprofile_dict[key]
            return initial
        else:
            return initial

    def form_valid(self, form):
        """If the form is valid it adds additional information to the form
        before saving the Order, such as Stripe PID, the original cart for
        reference and billing/shipping info.
        If an invalid item is somehow in the cart, it removes the order.
        It will delete the cart in the session.
        Attaches the user tot he order if logged in or adds a the order to the
        session so an anonymous user can access the Order Detail Page."""

        # Saves the form but doesn't commit it to the database yet.
        order = form.save(commit=False)
        # Fills in the STRIPE PID infor
        pid = self.request.POST.get('client_secret').split('_secret')[0]
        order.stripe_pid = pid
        # Dumps the original cart info
        cart_contents = get_cart(self.request)
        cart = cart_contents['cart']
        order.original_cart = json.dumps(cart)
        order.delivery_cost = cart_contents['delivery']
        # If billing and shipping info are the marked as the same, it fills in
        # the billing with the POST data. Clauses are used for optional info.
        if 'billing-same' in self.request.POST:
            order.billing_full_name = self.request.POST['shipping_full_name']
            order.billing_phone_number = self.request.POST[
                'shipping_phone_number_0'] + self.request.POST['shipping_phone_number_1']  # noqa E501
            order.billing_street_address_1 = self.request.POST['shipping_street_address_1']  # noqa E501
            if 'shipping_street_address_2' in self.request.POST:
                order.billing_street_address_2 = self.request.POST['shipping_street_address_2']  # noqa E501
            order.billing_town_or_city = self.request.POST['shipping_town_or_city']  # noqa E501
            if 'shipping_county' in self.request.POST:
                order.billing_county = self.request.POST['shipping_county']
            order.billing_country = self.request.POST['shipping_country']
            if 'shipping_postcode' in self.request.POST:
                order.billing_postcode = self.request.POST['shipping_postcode']
        order.save()

        # Iterates the items to create OrderLine Item objects.
        # If the product doesn't exist it deltes the order.
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
                messages.warning(self.request, (
                    "One of the products in your cart wasn't found in our collection. \
                    Please call us for assistance!")
                )
                order.delete()

        # Deetes the cart as it isn't needed.
        if 'cart' in self.request.session:
            del self.request.session['cart']

            # Attaches the order to a logged in user or adds the order to the
            # session.
            if self.request.user.is_authenticated:
                order.user_profile = self.request.user.userprofile
                order.save()
            else:
                self.request.session['my_order'] = order.id

        messages.success(self.request, f'Order successfully processed! \
             A confirmation email will be sent to {order.email}.')
        return super().form_valid(form)

    def form_invalid(self, form):
        """An invalid form returns the user to the order page with a mesage."""
        messages.warning(self.request, 'There was a problem processing the order. Please double check your information.')  # noqa E501
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        """Adds all necessary information to the context.
        IN particular, the Stripe info necessary for payment."""
        context = super().get_context_data(**kwargs)

        # Details necessary for Stripe payment processing
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart_contents = get_cart(self.request)
        total = cart_contents['grand_total']

        # Sets value to what is necessary for Stripe.
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Passes the custom order form to the page.
        order_form = context['form']

        context['stripe_public_key'] = stripe_public_key
        context['client_secret'] = intent.client_secret
        context['order_form'] = order_form
        return context


@require_POST
def cache_data(request):
    """Caches payment info and adds it to stripe metadata."""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'user': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.warning(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
