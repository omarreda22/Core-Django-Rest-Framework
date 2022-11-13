
from decimal import Decimal
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=225, null=True)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    @property
    def sell(self):
        try:
            return self.price * Decimal('0.8')
        except:
            return None

    def get_discount(self):
        return '10.00'
