from django import forms
from .models import Sale, SalesDetail

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ("customer",)
        widgets = {
            "customer": forms.Select(attrs={"class": "Customers__input", "placeholder": "Seleccione el cliente"}),
        }

class SalesDetailForm(forms.ModelForm):
    class Meta:
        model = SalesDetail
        fields = ("sale", "product", "quantity", "price_unit")
        widgets = {
            "sale": forms.Select(attrs={"class": "Sale__input", "placeholder": "Seleccione la venta"}),
            "product": forms.Select(attrs={"class": "Product__input", "placeholder": "Seleccione el producto"}),
            "quantity": forms.NumberInput(attrs={"class": "Quantity__input", "placeholder": "Ingrese la cantidad"}),
            "price_unit": forms.NumberInput(attrs={"class": "Price__input", "placeholder": "Ingrese el precio"}),
        }