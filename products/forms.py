from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'productCode', 'price', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product title'}),
            'productCode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product code'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
        }