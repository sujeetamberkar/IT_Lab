from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, AuthorForm, PublisherForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')  # Redirect as appropriate
    else:
        form = AuthorForm()
    return render(request, 'book/add_author.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')  # Redirect as appropriate
    else:
        form = PublisherForm()
    return render(request, 'book/add_publisher.html', {'form': form})
