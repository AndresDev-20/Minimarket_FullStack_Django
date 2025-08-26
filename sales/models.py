from django.db import models

# Create your models here.

class Sale(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT, related_name='sales', null=False)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=50, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"Sale {self.id} - {self.customer}"
    

class SalesDetail(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='sales_details', null=False)
    sale = models.ForeignKey('Sale', on_delete=models.CASCADE, related_name='details', null=False)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    subtotal = models.DecimalField(max_digits=30, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"
    
