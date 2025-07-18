from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Checker-specific views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # ✅ Class-based views (your original design, retained for extensibility)
    path('custom-login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('custom-logout/', views.CustomLogoutView.as_view(), name='custom_logout'),
    path('custom-register/', views.RegisterView.as_view(), name='custom_register'),
]

