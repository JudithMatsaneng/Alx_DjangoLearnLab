import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return None

# Example usage
if __name__ == "__main__":
    author_name = "John Doe"  # Replace with the actual author name
    books_by_author = query_books_by_author(author_name)
    if books_by_author:
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(book.title)
    else:
        print(f"No books found for author {author_name}")

    library_name = "My Library"  # Replace with the actual library name
    books_in_library = list_books_in_library(library_name)
    if books_in_library:
        print(f"\nBooks in {library_name}:")
        for book in books_in_library:
            print(book.title)
    else:
        print(f"No books found in {library_name}")



