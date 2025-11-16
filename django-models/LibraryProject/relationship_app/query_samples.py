from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author"""
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def list_library_books(library_name):
    """List all books in a library"""
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_library_librarian(library_name):
    """Retrieve the librarian for a library"""
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# Example usage:
"""
# Create test data
author = Author.objects.create(name="John Doe")
book = Book.objects.create(title="Sample Book", author=author)
library = Library.objects.create(name="Central Library")
library.books.add(book)
librarian = Librarian.objects.create(name="Jane Smith", library=library)

# Run queries
books = query_books_by_author("John Doe")
library_books = list_library_books("Central Library")
librarian = get_library_librarian("Central Library")
"""

# ...existing code...
from .models import Author, Book, Library, Librarian

def books_by_author(author_name):
    """Return queryset of books by author name."""
    return Book.objects.filter(author__name=author_name)

def books_in_library(library_name):
    """Return queryset of books in a library by library name."""
    return Book.objects.filter(libraries__name=library_name).distinct()

def librarian_for_library(library_name):
    """Return Librarian instance for named library (or None)."""
    try:
        lib = Library.objects.get(name=library_name)
        return getattr(lib, 'librarian', None)
    except Library.DoesNotExist:
        return None
# ...existing code...