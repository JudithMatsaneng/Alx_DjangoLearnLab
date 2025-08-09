from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookList(generics.ListAPIView):
    """
    GET /api/books/  -> returns list of all books in JSON
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
