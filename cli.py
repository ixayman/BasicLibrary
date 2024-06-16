import argparse
from library import Library
from book import Book


def main():

    parser = argparse.ArgumentParser(description="Personal Library Manager CLI")
    # Arguments for adding, listing, editing, and deleting books
    parser.add_argument('--add', nargs=4, metavar=('title', 'author', 'year', 'genre'), help='Add a new book')
    parser.add_argument('--list', action='store_true', help='List all books')
    parser.add_argument('--edit', nargs=5, metavar=('id', 'title', 'author', 'year', 'genre'), help='Edit a book')
    parser.add_argument('--delete', metavar='id', help='Delete a book')

    args = parser.parse_args()
    library = Library()
    library.load_from_file('data/library.json')
    args.add = input()
    # Handle the add book operation
    if args.add:
        title, author, year, genre = args.add
        library.add_book(Book(title, author, year, genre))
    # Handle the list books operation
    elif args.list:
        for book in library.list_books():
            print(book)
    # Handle the edit book operation
    elif args.edit:
        book_id, title, author, year, genre = args.edit
        new_book = Book(title, author, year, genre, book_id)
        library.edit_book(book_id, new_book)
    # Handle the delete book operation
    elif args.delete:
        library.delete_book(args.delete)

    # Save the library to file after any modifications
    library.save_to_file('data/library.json')


if __name__ == "__main__":
    main()
