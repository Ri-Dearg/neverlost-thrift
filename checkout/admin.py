from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """Setting for model on admin page."""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """Setting for model on admin page."""
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'email', 'date',
              'shipping_full_name', 'shipping_phone_number',
              'shipping_country', 'shipping_postcode', 'shipping_town_or_city',
              'shipping_street_address_1', 'shipping_street_address_2',
              'shipping_county', 'billing_full_name', 'billing_phone_number',
              'billing_country', 'billing_postcode', 'billing_town_or_city',
              'billing_street_address_1', 'billing_street_address_2',
              'billing_county', 'delivery_cost', 'order_total', 'grand_total',
              'original_cart', 'stripe_pid')

    list_display = ('order_number', 'date', 'billing_full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
