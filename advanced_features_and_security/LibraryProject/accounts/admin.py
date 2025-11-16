from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    """
    Custom admin interface for the CustomUser model.
    Includes the additional fields (date_of_birth, profile_photo).
    """
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Profile Information', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Profile Information', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    list_filter = BaseUserAdmin.list_filter + ('date_of_birth',)
    search_fields = ('username', 'email', 'first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)
