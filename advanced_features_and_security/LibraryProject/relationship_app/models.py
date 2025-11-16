from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        permissions = (
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        )

    def __str__(self):
        return f"{self.title}"

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries', blank=True)

    class Meta:
        permissions = (
            ("can_view", "Can view library"),
            ("can_create", "Can create library"),
            ("can_edit", "Can edit library"),
            ("can_delete", "Can delete library"),
        )

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=150)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"{self.name} ({self.library.name})"

class UserProfile(models.Model):
    """
    Extended user profile using the custom user model.
    Links to CustomUser instead of Django's default User.
    """
    ROLE_ADMIN = 'Admin'
    ROLE_LIB = 'Librarian'
    ROLE_MEMBER = 'Member'
    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_LIB, 'Librarian'),
        (ROLE_MEMBER, 'Member'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to automatically create a UserProfile when a new CustomUser is created.
    """
    if created:
        UserProfile.objects.get_or_create(user=instance)