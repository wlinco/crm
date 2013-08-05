from django.contrib import admin

from core.models import Product
from core.models import Customer
from core.models import Order
from core.models import ProductInOrder

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ProductInOrder)