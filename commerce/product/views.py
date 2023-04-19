from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import NewProductForm, EditProductForm
# Create your views here.

def products(request):
    products = Product.objects.filter(is_sold=False)
    return render(request, 'product/products.html', {
        'products': products
    })

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'product/detail.html', {
        'product': product,
        'related_products': related_products
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            
            return redirect('product:detail', pk=product.id)
        else: 
            form = NewProductForm()

    form = NewProductForm()
    
    return render(request, 'product/form.html', {
        'form': form,
        'title': 'New Product'
    })

@login_required
def edit(request, pk):

    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    # get_object_or_404 is a shortcut that will return a 404 error if the object is not found
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
       
        if form.is_valid():
            form.save()
            
            return redirect('product:detail', pk=product.id)
    else: 
            form = EditProductForm(instance=product)

    
    
    return render(request, 'product/form.html', {
        'form': form,
        'title': 'Edit Product'
    })

@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    product.delete()
    return redirect('dashboard:index')