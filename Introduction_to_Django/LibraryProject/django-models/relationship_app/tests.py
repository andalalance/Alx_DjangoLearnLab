from django.test import TestCase
from .models import Author, Book, Library, Librarian
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "John Doe")

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(title="Sample Book", author=self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Sample Book")
        self.assertEqual(self.book.author.name, "John Doe")

class LibraryModelTest(TestCase):
    def setUp(self):
        self.library = Library.objects.create(name="Central Library")
        self.book = Book.objects.create(title="Sample Book")
        self.library.books.add(self.book)

    def test_library_books(self):
        self.assertIn(self.book, self.library.books.all())

class LibrarianModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='librarian', password='password')
        self.library = Library.objects.create(name="Central Library")
        self.librarian = Librarian.objects.create(user=self.user, library=self.library)

    def test_librarian_creation(self):
        self.assertEqual(self.librarian.user.username, 'librarian')
        self.assertEqual(self.librarian.library.name, "Central Library")