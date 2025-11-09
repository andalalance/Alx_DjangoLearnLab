from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    template_name = 'bookshelf/book_form.html'
    fields = ['title', 'author', 'publication_year']
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'bookshelf/book_form.html'
    fields = ['title', 'author', 'publication_year']
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'bookshelf/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')