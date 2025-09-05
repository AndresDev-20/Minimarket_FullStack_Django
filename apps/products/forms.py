from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "name", "purchase_price", "sale_price", "description", "stock", "is_active")

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)