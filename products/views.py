# products/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@login_required
@never_cache
def list_products(request):
    products = Product.objects.all()
    #print(products[0].stock)
    return render(request, 'products/list_products.html', {'products': products})

@login_required
@never_cache
def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.save()
        return redirect('list_products')
    return render(request, 'products/update_product.html', {'product': product})

@login_required
@never_cache
def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        # Create and save the new product
        Product.objects.create(name=name, description=description, price=price, stock=stock)
        
        return redirect('list_products')
    
    return render(request, 'products/create_product.html')