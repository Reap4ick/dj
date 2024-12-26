from django import forms
from products.models import Product


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"  # all User model fields