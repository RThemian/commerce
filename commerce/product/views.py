from django.shortcuts import render, get_object_or_404
from product.models import Product

# Create your views here.

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)


    return render(request, 'product/detail.html', {
        'product': product
    })