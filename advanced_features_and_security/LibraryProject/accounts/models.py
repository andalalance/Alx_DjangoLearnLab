from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Adds additional fields for enhanced user profile functionality.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    objects = CustomUserManager()

    class Meta:
        permissions = (
            ("can_view", "Can view"),
            ("can_create", "Can create"),
            ("can_edit", "Can edit"),
            ("can_delete", "Can delete"),
        )

    def __str__(self):
        return f"{self.username}"
