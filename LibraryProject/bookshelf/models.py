from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    """
    Model representing a book in the library.

    Fields:
    - title: CharField with max_length of 200 characters.
    - author: CharField with max_length of 100 characters.
    - publication_year: IntegerField for the year of publication.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        """String representation for the Django Admin and shell."""
        return f"{self.title} by {self.author} ({self.publication_year})"
