from django.shortcuts import render, redirect
from checkout.forms import AddressForm
from cart.models import Order

import random
import string

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))



def checkout_view(request):
    form = AddressForm

    try:
        order_qs = Order.objects.filter(user = request.user, ordered=False)
        order = order_qs[0]

    except:
        return redirect('/')
        


    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            order.address = address
            order.code = create_ref_code()
            order.in_way= True
            order.ordered = True
            order.save()
            return redirect('/')
        else:
            print('error')

    template_name = 'checkout/checkout.html'
    context = {
        'form': form,
        'order':order
        }
    return render(request, template_name, context)