from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','category','quantity']
        labels={'name':'Name','category':'Category','quantity':'Quantity'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
        }

class OrderForm(forms.ModelForm):
        class Meta:
            model=Order
            fields=['product','order_quantity']
            widgets={
            'product':forms.Select(attrs={'class':'form-control'}),
            'order_quantity':forms.NumberInput(attrs={'class':'form-control'}),
        }
