from django.db import models

from django.contrib.auth.models import User

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    barcode = models.CharField(max_length=200)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    rr_price = models.DecimalField(max_digits=6, decimal_places=2)
    manufacturer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address_1 = models.CharField(max_length=256)
    address_2 = models.CharField(max_length=256, blank=True)
    address_3 = models.CharField(max_length=256, blank=True)
    suburb = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    #email = models.CharField(max_length=50, blank=True)
    #phone = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=20)
    points = models.IntegerField()
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    order_number = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.order_number)

class ProductInOrder(models.Model):
    pio_id = models.AutoField(primary_key=True)
    order_number = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)