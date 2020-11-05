from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from cart.models import CartItem, Order

import random
import string

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=25))

@login_required
def cart_view(request):
    order = get_object_or_404(Order, user=request.user, ordered= False)
    template_name = 'cart/cart.html'
    context = {"order":order}
    return render(request, template_name, context)

@login_required
def add_item_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_item, create = CartItem.objects.get_or_create(user= request.user, product=product)
    order_qs = Order.objects.filter(user= request.user, ordered=False)

    if  order_qs.exists():
        order = order_qs[0]

        if order.products.filter(product__slug = product.slug).exists():
            cart_item.quantity +=1
            cart_item.save()
            return redirect('cart:cart')

        else:
            order.products.add(cart_item)
            order.save()
            return redirect('cart:cart')
    else:
        order = Order.objects.create(user= request.user)
        order.products.add(cart_item)
        order.save()

        return redirect('cart:cart')

    return redirect('cart:cart')

@login_required
def delete_multi_products(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_item = get_object_or_404(CartItem,user=request.user, product=product)
    order_qs = Order.objects.filter(user= request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if cart_item in order.products.all():
            order.products.remove(cart_item)
            cart_item.quantity = 1
            cart_item.save()
            order.save()
            return redirect('cart:cart')

        else :
            return redirect('cart:cart')

    return redirect('/')

@login_required
def delete_single_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_item = get_object_or_404(CartItem,user=request.user, product=product)
    order_qs = Order.objects.filter(user= request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if cart_item in order.products.all():
            if cart_item.quantity > 1:
                cart_item.quantity -=1
                cart_item.save()
                return redirect('cart:cart')
            else:
                order.products.remove(cart_item)
                cart_item.quantity = 1
                cart_item.save()
                order.save()
                return redirect('cart:cart')


        else :
            return redirect('cart:cart')

    return redirect('/')