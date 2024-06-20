
def filter_entries(entries, search_query):
    search_query = search_query.lower()
    return [entry for entry in entries if search_query in entry['title'].lower() or
            search_query in entry['author'].lower() or
            search_query in entry['genre'].lower() or
            search_query in entry['publication_year']]

