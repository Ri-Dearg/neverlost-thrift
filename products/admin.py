from django.contrib import admin

from .models import Product, Category, StockDrop


class CategoryAdmin(admin.ModelAdmin):
    """Setting for model on admin page"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(StockDrop)
