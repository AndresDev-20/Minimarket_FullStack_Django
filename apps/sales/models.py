from django.db import models

# Create your models here.

class Sale(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT, related_name='sales', null=False)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=0)

    def __str__(self):
        return f"Sale {self.id} - {self.customer}"
    
    def calculate_total(self):
        total = sum(detail.subtotal for detail in self.details.all())
        self.total = total
        self.save()
    

class SalesDetail(models.Model):
    product = models.ForeignKey( 'products.Product', on_delete=models.PROTECT, related_name='sales_details', null=False )
    sale = models.ForeignKey('Sale', on_delete=models.CASCADE, related_name='details', null=False)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)

    # Precio unitario de venta (se autollenará desde el producto)
    price_unit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Precio unitario de compra (para calcular la ganancia)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    subtotal = models.DecimalField(max_digits=30, decimal_places=2)
    profit = models.DecimalField(max_digits=30, decimal_places=2, default=0)  # Ganancia

    def save(self, *args, **kwargs):
        # Siempre tomar los precios actuales del producto
        self.price_unit = self.product.sale_price
        self.purchase_price = self.product.purchase_price

        # Subtotal = cantidad * precio de venta
        self.subtotal = self.quantity * self.price_unit

        # Ganancia = (precio venta - precio compra) * cantidad
        self.profit = (self.price_unit - self.purchase_price) * self.quantity

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

    
