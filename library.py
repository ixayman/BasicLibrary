import json
from book import Book


class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, book):
        # Add a Book instance to the library
        self.books.append(book)

    def list_books(self, filter_by=None, filter_value=None):
        # List all books or filter them by a specific attribute (author or genre)
        if not filter_by:
            return self.books
        else:
            return [book for book in self.books if getattr(book, filter_by) == filter_value]

    def edit_book(self, book_id, new_book):
        # Edit the details of a book with the given book ID
        for i, book in enumerate(self.books):
            if book.book_id == book_id:
                self.books[i] = new_book
                return

    def delete_book(self, book_id):
        # Delete a book with the given book ID
        self.books = [book for book in self.books if book.book_id != book_id]

    def save_to_file(self, filename):
        # Save the list of books to a JSON file
        with open(filename, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file)

    def load_from_file(self, filename):
        # Load the list of books from a JSON file
        try:
            with open(filename, 'r') as file:
                book_dicts = json.load(file)
                self.books = [Book.from_dict(book_dict) for book_dict in book_dicts]
        except FileNotFoundError:
            # If the file is not found, initialize an empty list of books
            self.books = []