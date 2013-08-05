from django.forms import ModelForm, TextInput, Textarea
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

class OrderForm(ModelForm):
    class Meta:
        model = Order
        #OrderFormSet = inlineformset_factory(Order, ProductInOrder)