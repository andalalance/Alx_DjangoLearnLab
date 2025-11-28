from rest_framework import serializers
from datetime import date
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields and validates publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ("id", "title", "publication_year", "author")

    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author and nests related books using BookSerializer.
    The 'books' field uses related_name='books' from Book.author FK.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ("id", "name", "books")