from django.urls import path
from . import views

# Setting app_name allows you to refer to URLs like 'bookshelf:index'
app_name = 'bookshelf'

urlpatterns = [
    # Placeholder path for the main index page of the app
    # (e.g., accessed at http://127.0.0.1:8000/)
    path('', views.index, name='index'), 
]

# Note: The 'index' view function must be created in bookshelf/views.py
