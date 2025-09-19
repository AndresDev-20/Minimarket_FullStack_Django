from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "phone", "address", "is_active")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "Customer__input", "placeholder": "Ingrese el nombre"}),
            "last_name": forms.TextInput(attrs={"class": "Customer__input", "placeholder": "Ingrese el apellido"}),
            "email": forms.EmailInput(attrs={"class": "Customer__input", "placeholder": "Ingrese el email"}),
            "phone": forms.TextInput(attrs={"class": "Customer__input", "placeholder": "Ingrese el teléfono"}),
            "address": forms.TextInput(attrs={"class": "Customer__input", "placeholder": "Ingrese la dirección"}),
        }