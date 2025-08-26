from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    contact_person = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    address = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name
    
class Buys(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"Buy from {self.supplier.name} on {self.date}"

class BuysDetail(models.Model):
    buy = models.ForeignKey(Buys, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"