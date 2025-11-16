from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.
    Handles user creation with additional fields.
    """
    
    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        """
        Create a regular user with the given credentials and optional fields.
        """
        if not email:
            raise ValueError("The Email field is required")
        if not username:
            raise ValueError("The Username field is required")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_photo=profile_photo
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        """
        Create a superuser with the given credentials and optional fields.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user