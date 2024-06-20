from filemgmt import save_entries, load_entries
from flask import Flask, render_template, request, redirect, flash, url_for
from add import add_book_to_library
from update import update_book, update_book_page, delete_book
from search import filter_entries


class FlaskApp:
    app = Flask(__name__, template_folder='templates')
    app.secret_key = '10/10noncrackablekey'

    @staticmethod
    @app.route('/')
    def home():
        entries = load_entries()
        # Get search and sorting parameters from the query string
        search_query = request.args.get('search', '')
        sort_by = request.args.get('sort_by', 'title')
        sort_order = request.args.get('sort_order', 'asc')

        # Filter entries based on search query
        if search_query:
            entries = filter_entries(entries, search_query)

        # Sort the entries based on the sorting parameters
        reverse = True if sort_order == 'desc' else False
        entries = sorted(entries, key=lambda x: x[sort_by], reverse=reverse)

        return render_template('home.html', entries=entries, sort_by=sort_by,
                               sort_order=sort_order, search_query=search_query)

    @staticmethod
    @app.route('/add_book_page')
    def add_book_page():
        return render_template('add_book.html')

    @staticmethod
    @app.route('/add_book', methods=['POST'])
    def add_book():
        return add_book_to_library(request)

    @staticmethod
    @app.route('/update_book_page/<int:book_id>')
    def update_book_page_route(book_id):
        return update_book_page(book_id)

    @staticmethod
    @app.route('/update_book/<int:book_id>', methods=['POST'])
    def update_book_route(book_id):
        return update_book(request, book_id)

    @staticmethod
    @app.route('/delete_book/<int:book_id>', methods=['POST'])
    def delete_book_route(book_id):
        return delete_book(book_id)

    @staticmethod
    def run():
        FlaskApp.app.run(debug=True)


if __name__ == '__main__':
    FlaskApp.run()
