from django.shortcuts import render, redirect
from .forms import CategoryForm, PageForm
from .models import Category

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # Updated redirect
            return redirect('dict:index')
    else:
        form = CategoryForm()
    return render(request, 'dict/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # Ensure this redirect is also correctly namespaced
            return redirect('dict:index')
    else:
        form = PageForm()
    return render(request, 'dict/add_page.html', {'form': form})

def index(request):
    categories = Category.objects.all()
    context_dict = {'categories': categories}
    return render(request, 'dict/index.html', context=context_dict)
