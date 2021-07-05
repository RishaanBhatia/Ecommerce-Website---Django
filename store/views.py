from django.shortcuts import get_object_or_404, render
from category.models import Category
from .models import Product
from random import randint

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug!=None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products':products,
        'product_count':product_count
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    products = Product.objects.all().filter(is_available=True)
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except exception as e:
        raise e

    product_number = randint(100, 999)

    context = {
        'single_product':single_product,
        'product_number':product_number,
        'total_products':len(products)
    }
    return render(request, 'store/product_detail.html', context)
