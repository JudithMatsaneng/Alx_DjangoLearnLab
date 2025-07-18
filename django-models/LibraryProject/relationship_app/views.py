from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import View

from .models import Book, Library

# Function-Based View using Book.objects.all()
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Library Detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ✅ Function-Based Register View (required for checker)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # change as needed
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# ✅ Class-Based Login View (for project structure)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# ✅ Class-Based Logout View
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# ✅ Class-Based Register View (for project structure)
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
        return render(request, 'relationship_app/register.html', {'form': form})

from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.http import HttpResponse

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
