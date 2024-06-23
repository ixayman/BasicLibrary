from flask import flash, redirect, url_for
from filemgmt import load_entries, save_entries
# added for pull request

def add_book_to_library(request):
    title = request.form['title']
    author = request.form['author']
    publication_year = request.form['publication_year']
    genre = request.form['genre']
    count = request.form['count']

    # Validate input
    if not (title and author and genre):
        flash('Title, author, and genre must be non-empty strings.')
        return redirect(url_for('add_book_page'))
    if not (-2000 <= int(publication_year) <= 2024):
        flash('Publication year must be between -2000 and 2024.')
        return redirect(url_for('add_book_page'))
    if not (1 <= int(count) <= 999):
        flash('Count must be between 1 and 999.')
        return redirect(url_for('add_book_page'))

    # Load the current data
    entries = load_entries()

    # Check for duplicate entry
    for entry in entries:
        if (entry['title'] == title and entry['author'] == author and
                entry['publication_year'] == publication_year and entry['genre'] == genre):
            flash('A book with the same title, author, publication year, and genre already exists.')
            return redirect(url_for('add_book_page'))

    # Generate a new unique ID for the new book
    new_id = max(entry['id'] for entry in entries) + 1 if entries else 1

    # Add the new book
    new_entry = {
        "id": new_id,
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "count": int(count)
    }
    entries.append(new_entry)
    save_entries(entries)

    flash('Book added successfully!')
    return redirect(url_for('home'))
