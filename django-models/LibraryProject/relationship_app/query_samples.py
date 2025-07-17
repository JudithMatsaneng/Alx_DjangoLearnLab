from django.apps import apps

Author = apps.get_model('relationship_app', 'Author')
Book = apps.get_model('relationship_app', 'Book')

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

# Example usage
if __name__ == "__main__":
    author_name = "John Doe"  # Replace with the actual author name
    books = query_books_by_author(author_name)
    if books:
        print(f"Books by {author_name}:")
        for book in books:
            print(book.title)
    else:
        print(f"No books found for author {author_name}")

