from django.urls import path
from .views import AuthorList, BookList
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail-update-delete'),
]

"""
BookListCreateView:
- GET: List all books, accessible by anyone.
- POST: Create a new book, restricted to authenticated users.

BookRetrieveUpdateDestroyView:
- GET: Retrieve details of a single book by its ID.
- PUT/PATCH: Update a book, restricted to authenticated users.
- DELETE: Delete a book, restricted to authenticated users.

Permissions:
- Uses IsAuthenticatedOrReadOnly, ensuring safe read access for all and write access only for authenticated users.
"""
