from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
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
    path('member-view/', views.member_view, name='member_view'),]
   
urlpatterns += [
    # ✅ Book management views-SECURED VIEWS
    path('book/add/', BookCreateView.as_view(), name='add_book'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='edit_book'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book'),
]


