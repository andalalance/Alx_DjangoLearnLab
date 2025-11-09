from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

    class Meta:
        permissions = [
            ("can_view_profile", "Can view user profile"),
            ("can_edit_profile", "Can edit user profile"),
        ]