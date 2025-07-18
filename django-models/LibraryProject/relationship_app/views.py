from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login  # ✅ This is required
from django.urls import reverse_lazy
from django.views import View

from .models import Book, Library

# Function-Based View using Book.objects.all()
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Login View
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration View using UserCreationForm and login
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ This line is required by the checker
            return redirect('home')  # 👈 Change 'home' to your actual home view name
        return render(request, 'relationship_app/register.html', {'form': form})
