from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Book views using DRF generic views
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET /api/books/  -> list books (supports filtering, search, ordering)
    POST /api/books/ -> create book (authenticated required)
    """
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["publication_year", "author__name", "title"]
    search_fields = ["title", "author__name"]
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET/PUT/DELETE /api/books/<pk>/
    Create/Update/Delete require authentication (permission class enforces write access).
    """
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Author views
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.prefetch_related("books").all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.prefetch_related("books").all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]