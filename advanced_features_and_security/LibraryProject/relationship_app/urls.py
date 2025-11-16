from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Book views
    path('books/', views.book_list, name='book-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('book/add/', views.add_book, name='book-add'),
    path('book/<int:pk>/edit/', views.edit_book, name='book-edit'),
    path('book/<int:pk>/delete/', views.delete_book, name='book-delete'),
    
    # Authentication views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Role-based views
    path('admin-view/', views.admin_view, name='admin-view'),
    path('librarian-view/', views.librarian_view, name='librarian-view'),
    path('member-view/', views.member_view, name='member-view'),
]