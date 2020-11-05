from django.db import models
from products.models import Product
from django.conf  import settings

User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    created_at = models.TimeField( auto_now_add=True)

    def __str__(self):
        return self.product.name
    
    def total_price(self):
        total = float(self.product.price) * float(self.quantity)
        return total

    def total_discount(self):
        if self.product.old_price:
            total = (float(self.product.old_price) - float(self.product.price)) * float(self.quantity)
        else:
            total = 0
        return total

    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    code    = models.CharField(max_length= 25)
    ordered = models.BooleanField(default=False)
    created_at = models.TimeField( auto_now_add=True)

    def __str__(self):
        return self.user.username

    
    def order_price(self):
        total = 0
        for cart_item in self.products.all():
            total += float(cart_item.total_price())

        return total

    def order_discount(self):
        total = 0
        for cart_item in self.products.all():
            total += float(cart_item.total_discount())

        return total

    def subtotal(self):
        total = int(self.order_discount()) + int(self.order_price())
        return total