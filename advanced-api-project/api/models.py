from django.db import models

class Author(models.Model):
    """
    Author model stores author name and is the parent in Author -> Book relationship.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book entity.
    - title: book title string
    - publication_year: integer (year)
    - author: ForeignKey to Author (one-to-many)
    related_name='books' used for nested serialization convenience.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"