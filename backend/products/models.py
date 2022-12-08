
from decimal import Decimal
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
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
