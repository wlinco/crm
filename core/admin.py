from django.contrib import admin

from core.models import Product
from core.models import Customer
from core.models import Order
from core.models import ProductInOrder

class ProductInline(admin.TabularInline):
    model = ProductInOrder
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(Order,OrderAdmin)

admin.site.register(Product)
admin.site.register(Customer)
#admin.site.register(ProductInOrder)
#admin.site.register(OrderAdmin)
