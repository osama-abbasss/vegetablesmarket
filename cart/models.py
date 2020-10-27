from django.db import models
from products.models import Product
from django.conf  import settings

User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered = models.BooleanField(default=False)
    created_at = models.TimeField( auto_now_add=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ManyToManyField(CartItem)
    code    = models.CharField(max_length= 25)
    ordered = models.BooleanField(default=False)
    created_at = models.TimeField( auto_now_add=True)

    def __str__(self):
        return self.code