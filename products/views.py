from django.shortcuts import render, get_object_or_404
from products.models import Product


def index(request):

    template_name = 'products/index.html'
    context = {}

    return render(request, template_name, context)



def all_products_view(request):
    all_products = Product.objects.all()

    template_name = 'products/all_products.html'
    context = {
        'products':all_products,
        }

    return render(request, template_name, context)


def single_product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    template_name = 'products/product_single.html'
    context = {
        'product':product,
        }

    return render(request, template_name, context)

