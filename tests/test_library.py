import unittest
from library import Library
from book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        # Set up a Library instance and sample Book instances for testing
        self.library = Library()
        self.book1 = Book("1984", "George Orwell", 1949, "Dystopian")
        self.book2 = Book("Brave New World", "Aldous Huxley", 1932, "Science Fiction")

    def test_add_book(self):
        # Test adding a book to the library
        self.library.add_book(self.book1)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "1984")

    def test_list_books(self):
        # Test listing all books in the library
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        books = self.library.list_books()
        self.assertEqual(len(books), 2)

    def test_edit_book(self):
        # Test editing a book's details in the library
        self.library.add_book(self.book1)
        new_book = Book("Animal Farm", "George Orwell", 1945, "Political Satire", self.book1.book_id)
        self.library.edit_book(self.book1.book_id, new_book)
        self.assertEqual(self.library.books[0].title, "Animal Farm")

    def test_delete_book(self):
        # Test deleting a book from the library
        self.library.add_book(self.book1)
        self.library.delete_book(self.book1.book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_save_and_load(self):
        # Test saving and loading the library from a file
        self.library.add_book(self.book1)
        self.library.save_to_file('test_library.json')
        new_library = Library()
        new_library.load_from_file('test_library.json')
        self.assertEqual(len(new_library.books), 1)
        self.assertEqual(new_library.books[0].title, "1984")

if __name__ == '__main__':
    unittest.main()