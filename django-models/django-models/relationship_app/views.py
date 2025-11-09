from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list.html', {'books': books})

class LibraryDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        library = get_object_or_404(Library, pk=pk)
        return render(request, 'relationship_app/detail.html', {'library': library})