from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:index')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})

def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})
