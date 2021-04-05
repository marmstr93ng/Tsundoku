import pytest
from src.google_books import API

api = API()

@pytest.mark.parametrize("isbn, expected_result, test_info", [
    ("9781444165159", False, "Valid ISBN 13"), 
    ("1888799978", False, "Valid ISBN 10"),
    ("9781444165155", True, "Wrong ISBN 13 check digit"),
    ("1888799975", True, "Wrong ISBN 10 check digit"),
    ("14441651", False, "Wrong length"),
    ("9781444165A59", True, "Invalid char"),
    ("123456789X", False, "Valid ISBN 10 with X as check digit"),
    ("188X799978", True, "Invalid X char"),
])

def test_no_exception(isbn, expected_result, test_info):
    try:
        json_data = api.search(isbn)
    except Exception as exc:
        assert False, "Exception raise - {}".format(exc)
    
    assert (json_data["totalItems"] == 0) == expected_result
