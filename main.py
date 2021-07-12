import logging
import logging.config
import json
from src.google_books import GoogleBooks
from src.isbn import validate_isbn

def main():
    logging.config.fileConfig('logging/log_settings.conf')

    google_books = GoogleBooks()
    isbn = "9781444165159"
    if validate_isbn(isbn):
        try:
            json_data = google_books.search(isbn)
        except Exception as e:
            print(e)
        logging.debug("\n{}".format(json.dumps(json_data, indent=4)))

if __name__ == '__main__':
    main()