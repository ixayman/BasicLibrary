import unittest
from book import Book


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("1984", "George Orwell", 1949, "Dystopian")
        self.assertEqual(book._title, "1984")
        self.assertEqual(book._author, "George Orwell")
        self.assertEqual(book._publication_year, 1949)
        self.assertEqual(book._genre, "Dystopian")

    def test_book_to_dict(self):
        book = Book("1984", "George Orwell", 1949, "Dystopian")
        book_dict = book.to_dict()
        expected = {
            'title': "1984",
            'author': "George Orwell",
            'publication_year': 1949,
            'genre': "Dystopian"
        }
        self.assertEqual(book_dict, expected)

    def test_book_from_dict(self):
        book_dict = {
            'title': "1984",
            'author': "George Orwell",
            'publication_year': 1949,
            'genre': "Dystopian"
        }
        book = Book.from_dict(book_dict)
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(book.publication_year, 1949)
        self.assertEqual(book.genre, "Dystopian")


if __name__ == '__main__':
    unittest.main()
