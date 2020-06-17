from django.contrib import admin

from .models import Order, OrderLineItem


admin.site.register(Order)
admin.site.register(OrderLineItem)
