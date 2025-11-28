from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass1234")
        self.client = APIClient()
        self.author = Author.objects.create(name="Author A")
        self.book1 = Book.objects.create(title="Book One", publication_year=2000, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2010, author=self.author)

    def test_list_books(self):
        url = reverse("api:book-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.json()), 2)

    def test_create_book_requires_auth(self):
        url = reverse("api:book-list")
        data = {"title": "New Book", "publication_year": 2020, "author": self.author.id}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        # authenticate and try again
        self.client.force_authenticate(self.user)
        resp2 = self.client.post(url, data)
        self.assertEqual(resp2.status_code, status.HTTP_201_CREATED)

    def test_filter_search_order(self):
        url = reverse("api:book-list")
        resp = self.client.get(url + "?search=One")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.json()), 1)
        resp2 = self.client.get(url + "?ordering=-publication_year")
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)
        years = [b["publication_year"] for b in resp2.json()]
        self.assertTrue(years[0] >= years[1])

    def test_publication_year_validation(self):
        url = reverse("api:book-list")
        self.client.force_authenticate(self.user)
        future_year = 3000
        data = {"title": "Future Book", "publication_year": future_year, "author": self.author.id}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("publication_year", resp.json())