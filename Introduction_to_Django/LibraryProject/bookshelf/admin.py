from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

# Register the Book model and customize its appearance in the Admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Book model in the Django admin interface.
    """
    # 1. Customize the list view columns
    list_display = (
        'title',
        'author',
        'publication_year'
    )

    # 2. Configure list filters (for the right sidebar)
    list_filter = (
        'publication_year',
        'author',
    )

    # 3. Configure search capabilities (searches the specified fields)
    search_fields = (
        'title',
        'author',
    )

    # 4. Make the publication year field editable directly from the list page
    list_editable = (
        'publication_year',
    )
