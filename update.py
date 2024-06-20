from flask import flash, redirect, url_for, render_template
from filemgmt import load_entries, save_entries


# Find the book by id
def update_book(request, book_id):
    entries = load_entries()
    book_index = next((index for index, entry in enumerate(entries) if entry['id'] == book_id), None)
    if book_index is not None:
        entries[book_index] = {
            "id": book_id,
            "title": request.form['title'],
            "author": request.form['author'],
            "publication_year": request.form['publication_year'],
            "genre": request.form['genre'],
            "count": int(request.form['count'])
        }
        save_entries(entries)
        flash('Book updated successfully!')
    else:
        flash('Invalid book ID.')

    return redirect(url_for('home'))


def update_book_page(book_id):
    entries = load_entries()
    # Find the book by id
    book = next((entry for entry in entries if entry['id'] == book_id), None)
    if book:
        return render_template('update_book.html', book=book, book_id=book_id)
    else:
        flash('Invalid book ID.')
        return redirect(url_for('home'))


def delete_book(book_id):
    entries = load_entries()
    # Find the book by id
    book_index = next((index for index, entry in enumerate(entries) if entry['id'] == book_id), None)
    if book_index is not None:
        del entries[book_index]
        save_entries(entries)
        flash('Book deleted successfully!')
    else:
        flash('Invalid book ID.')

    return redirect(url_for('home'))
