from django import forms
from products.models import Category, Product

class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"  # all User model fields
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
        }