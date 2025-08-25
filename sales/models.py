from django.db import models
from ..products.models import Product

# Create your models here.
class SalesDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sales_details', null=False)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    subtotal = models.DecimalField(max_digits=30, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"
    
class Sale(models.Model):
    sale_detail = models.ForeignKey(SalesDetail, on_delete=models.PROTECT, related_name='sales', null=False)
    date = models.DateTimeField(auto_now_add=True)
    