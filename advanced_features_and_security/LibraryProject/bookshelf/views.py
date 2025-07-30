from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from django import forms

# Simple BookForm for add/edit views
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

# View to list all books - requires login
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

# View to add a new book - requires permission can_create
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Add'})

# View to edit an existing book - requires permission can_edit
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Edit'})

# View to delete a book - requires permission can_delete
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

from django.shortcuts import render
from .models import Book
from .forms import ExampleForm
from .forms import BookSearchForm

def book_list(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        title = form.cleaned_data.get('title')
        if title:
            books = books.filter(title__icontains=title)

    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})

