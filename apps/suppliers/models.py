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
    
