from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, add_book, edit_book, delete_book, register, CustomLoginView, CustomLogoutView, RegisterView



urlpatterns = [
    # ✅ Basic views for your project
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Auth views for checker
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # ✅ Custom views for your project
    path('custom-login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('custom-logout/', views.CustomLogoutView.as_view(), name='custom_logout'),
    path('custom-register/', views.RegisterView.as_view(), name='custom_register'),

    # ✅ Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    
    # ✅ Custom secured book actions
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
     
    
  ]


