from django.contrib import admin

from .models import (
    Order,
    ProductSets,
    Recipient
)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_created_datetime',)


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductSets)
admin.site.register(Recipient)
