from django.shortcuts import render
# import models from product app, not from core app
from product.models import Product, Category

# Create your views here.
def index(request):
    products = Product.objects.filter(is_sold=False)[0:6] # get first 6 products
    categories = Category.objects.all()
    return render(request, 'core/index.html', { 
        'categories': categories,
        'products': products
        })

def contact(request):
    return render(request, 'core/contact.html')

