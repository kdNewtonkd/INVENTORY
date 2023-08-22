from django import forms
from .models import Product


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