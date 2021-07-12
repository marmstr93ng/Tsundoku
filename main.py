import logging
import logging.config
import json
from src.google_books import GoogleBooks
from src.isbn import validate_isbn

def main():
    logging.config.fileConfig('logging/log_settings.conf')

    google_books = GoogleBooks()

    isbn = "14441651"
    logging.info("Validating ISBN:{}".format(isbn))
    valid_isbn_result_bool, valid_isbn_result_str = validate_isbn(isbn)


    if not valid_isbn_result_bool:
        logging.error("\t{}".format(valid_isbn_result_str))
    else:
        logging.info("\t{}".format(valid_isbn_result_str))

        logging.info("Retrieving Google Books information for ISBN:{}".format(isbn))
        try:
            json_data = google_books.search(isbn)
        except Exception as e:
            logging.info(e)
        logging.debug("\n{}".format(json.dumps(json_data, indent=4)))

if __name__ == '__main__':
    main()