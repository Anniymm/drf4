from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100) # varchar(100)
    price = models.DecimalField(max_digits=6, decimal_places=2) #decimal(6, 2)
    in_stock = models.BooleanField(default=True) #BOOLEAN

    def __str__(self):
        return self.name




