from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField(null=True, blank=True)
    
    class Meta:
        permissions = (
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        )
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.library.name}"

class UserProfile(models.Model):
    ROLES = [
        ('ADMIN', 'Admin'),
        ('LIBRARIAN', 'Librarian'),
        ('MEMBER', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLES, default='MEMBER')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Create your models here.
