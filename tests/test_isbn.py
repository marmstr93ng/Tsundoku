import sys
sys.path.insert(0, '../')

import pytest
from isbn import validate_isbn, convert_isbn_10_to_13, convert_isbn_13_to_10

@pytest.mark.parametrize("isbn, expected_result, test_info", [
    ("9781444165159", True, "Valid ISBN 13"), 
    ("1888799978", True, "Valid ISBN 10"),
    ("9781444165155", False, "Wrong ISBN 13 check digit"),
    ("1888799975", False, "Wrong ISBN 10 check digit"),
    ("14441651", False, "Wrong length"),
    ("9781444165A59", False, "Invalid char"),
    ("123456789X", True, "Valid ISBN 10 with X as check digit"),
    ("188X799978", False, "Invalid X char"),
])

def test_validate_isbn(isbn, expected_result, test_info):
    print(test_info)
    assert validate_isbn(isbn) == expected_result

@pytest.mark.parametrize("isbn_10, isbn_13", [
    ("0716020882", "9780716020882"), 
    ("1888799978", "9781888799972"),
    ("123456789X", "9781234567897"),
])

def test_convert_isbn_10_to_13(isbn_10, isbn_13):
    assert convert_isbn_10_to_13(isbn_10) == isbn_13

@pytest.mark.parametrize("isbn_13, isbn_10", [
    ("9780716020882", "0716020882"), 
    ("9781888799972", "1888799978"),
    ("1234567891234", None),
    ("9781234567897", "123456789X"),
])

def test_convert_isbn_13_to_10(isbn_13, isbn_10):
   assert convert_isbn_13_to_10(isbn_13) == isbn_10

# google_books_data
# def test_google_books_data():
#     results = google_books_data("0716020882")
#     match = False
#     print(type(results))
#     #if isinstance(results, Response)
#     for result in results['items']:
#         if result['volumeInfo']['title'] == "The Right Way to Play Chess":
#             match = True
#     assert match

