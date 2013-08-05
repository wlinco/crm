import datetime

from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.timezone import utc
from django.contrib.auth.decorators import login_required

from core.models import Customer
from core.models import Product
from core.models import Order
from core.models import ProductInOrder

from core.forms import ProductForm
from core.forms import UserForm
from core.forms import CustomerForm
from core.forms import OrderForm


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


def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return HttpResponseRedirect('/orders')
    else:
        form = OrderForm()
    return render(request, 'orders/new_order.html', {'form':form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html',{
        'orders': orders,
    })
