from django.shortcuts import render
from products.models import Product
from cart.models import CartItem, Order

import random
import string

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=25))

