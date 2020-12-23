from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.core.paginator import Paginator
from products.filters import ProductFilter


def index(request):
    products = Product.objects.all()[:6]
    template_name = 'products/index.html'
    context = {'products': products}
    return render(request, template_name, context)



def all_products_view(request):
    products_list = Product.objects.all()
    f = ProductFilter(request.GET, queryset=products_list)
    products_list = f.qs

    paginator = Paginator(products_list, 8) 
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    template_name = 'products/index.html'
    
    context = {'products': products, "f": f, 'products_list':products_list}
    template_name = 'products/all_products.html'
    return render(request, template_name, context)


def single_product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category= product.category)[:5]
    template_name = 'products/product_single.html'
    context = {
        'product':product,
        'related_products': related_products
        }

    return render(request, template_name, context)

