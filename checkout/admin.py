from django.contrib import admin
from .models import Order, OrderLineItem

"""
Build the checkout admin form based on Rob Simons' MS4 project.
"""


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
