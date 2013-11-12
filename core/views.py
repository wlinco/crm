import datetime

from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.timezone import utc
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory

from core.models import Customer
from core.models import Product
from core.models import Order
from core.models import ProductInOrder

from core.forms import ProductForm
from core.forms import UserForm
from core.forms import CustomerForm
from core.forms import OrderForm, OrderFormSet


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html',{
        'products': products,
    })

def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return HttpResponseRedirect('/products')
    else:
        form = ProductForm()
    return render(request, 'products/new_product.html', {'form':form})


def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/users')
    else:
        form = UserForm()
    return render(request,'users/new_user.html', {'form':form})


def new_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return HttpResponseRedirect('/customer')
    else:
        form = CustomerForm()
    return render(request, 'customers/new_customer.html', {'form':form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html',{
        'customers': customers,
    })

def customer(request,id):
   customer = Customer.objects.get(customer_id=id)
   customer_orders = Order.objects.filter(customer_id=id)
   total_orders = len(Order.objects.filter(customer_id=id))
  
   backordered_items = []
   customer_backorders = 0
   customer_total = 0
   for orders in customer_orders:
       customer_total += orders.order_total
       line_items = ProductInOrder.objects.filter(order_number = orders.order_number)
       for item in line_items:
           if item.is_backorder:
               customer_backorders += item.quantity 
               backordered_items.append(item)


   return render(request, 'customers/customer.html',{
       'customer': customer,
       'customer_orders': customer_orders,
       'total_orders': total_orders,
       'customer_total': customer_total,
       'total_backorders':customer_backorders,
       'backorder_list':backordered_items,
   })


def new_order(request):
    if request.method == 'POST':
        if 'add_product' in request.POST:
            the_order = Order.objects.get(pk=1)
            AddProductFormset = inlineformset_factory(Order,ProductInOrder,extra=0)
            customer_id = '0'
            if request.POST['customer_id'] != "":
                customer_id = request.POST['customer_id']
            #AddProductFormset = OrderFormSet()
            print "customer id is " + customer_id
            cp = request.POST.copy()
            cp['productinorder_set-TOTAL_FORMS'] = int(cp['productinorder_set-TOTAL_FORMS'])+ 1
            form = OrderForm()
            product_form = AddProductFormset(cp,instance=Order())
        else:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                product_form = OrderFormSet(request.POST, instance=order)

                if product_form.is_valid():
                    order.save()
                    product_form.save()
                    return HttpResponseRedirect('/orders')

    else:
        customer_id = '0'
        form = OrderForm()
        product_form = OrderFormSet(instance=Order())
    return render(request, 'orders/new_order.html', {'form':form, 'product_form':product_form,'customer_id':customer_id})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html',{
        'orders': orders,
    })


def price_lookup(request,id):
    product = Product.objects.filter(product_id=id)

    price = float(product[0].sale_price)
    to_json = {
        "price": price
    }
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')


def points_lookup(request,id):
    customer = Customer.objects.filter(customer_id=id)

    points = int(customer[0].points)
    to_json = {
        "points": points
    }
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

