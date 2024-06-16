import json
import uuid


class Book:
    def __init__(self, title, author, publication_year, genre, book_id=None):
        # Initialize a Book instance with title, author, publication year, genre, and a unique book ID
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._genre = genre
        # If book_id is not provided, generate a new unique ID
        self._book_id = book_id if book_id else str(uuid.uuid4())

    def to_dict(self):
        # Convert the Book instance to a dictionary for easy serialization
        return {
            'title': self._title,
            'author': self._author,
            'publication_year': self._publication_year,
            'genre': self._genre,
            'book_id': self._book_id
        }

    @classmethod
    def from_dict(cls, data):
        # Create a Book instance from a dictionary
        return cls(data['title'], data['author'], data['publication_year'], data['genre'], data['book_id'])

    def __str__(self):
        return f"{self._title} by {self._author}, {self._publication_year} - {self._genre}"
