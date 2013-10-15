from django.forms import ModelForm, TextInput, Textarea, Select
from django.forms.models import inlineformset_factory

from core.models import Product
from core.models import User
from core.models import Customer
from core.models import Order
from core.models import ProductInOrder

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name','sku','barcode','description','sale_price','rr_price','manufacturer',)
        widgets = {
            'name': TextInput(attrs={'class': 'required'}),
            'sku': TextInput(attrs={'class': 'required'}),
            'barcode': TextInput(attrs={'class': 'required'}),
            'description': Textarea(attrs={'class': 'required'}),
            'sale_price': TextInput(attrs={'class': 'required'}),
            'rr_price': TextInput(attrs={'class': 'required'}),
            'manufacturer': TextInput(attrs={'class': 'required'}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User

class CustomerForm(ModelForm):
    class Meta:
        model = Customer


OrderFormSet = inlineformset_factory(Order, ProductInOrder,extra=1)


class OrderForm(ModelForm):
    class Meta:
        model = Order

        fields = ('customer_id','order_total','comments',)
        widgets = {
            'customer_id': Select(attrs={'class':'form-control select2me','data-placeholder':'Search Customers'}),
            'comments': Textarea(attrs={'class':'order-comments','placeholder':'Comments'}),
            'order_total': TextInput(attrs={'value':'0'}),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer_id'].empty_label = 'Search'
