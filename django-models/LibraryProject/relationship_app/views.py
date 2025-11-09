from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.decorators import method_decorator
from .models import Book, Library, UserProfile

@login_required
def book_list(request):
    """Function-based view to list all books"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """Class-based view to show library details"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def is_admin(user):
    return user.userprofile.role == 'ADMIN'

def is_librarian(user):
    return user.userprofile.role == 'LIBRARIAN'

def is_member(user):
    return user.userprofile.role == 'MEMBER'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Create your views here.
