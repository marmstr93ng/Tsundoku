from typing import List, Tuple


def _cast_str_to_int_array(string: str) -> List[int]:
    int_array = []
    for value in string:
        if value.upper() == "X":
            int_array.append(10)
        else:
            int_array.append(int(value))
    return int_array

def _cast_int_array_to_str(int_array: List[int]) -> str:
    string = ""
    for value in int_array:
        if value == 10:
            string += "X"
        else:
            string += str(value)
    return string

def _isbn_13_weighted_sum(isbn_array: List[int]) -> Tuple[int, int]:
    sum_evens = 0
    sum_odds = 0
    for index, digit in enumerate(isbn_array):
        if ((index + 1) % 2) == 0:
            sum_evens += (digit * 3)
        else:
            sum_odds += digit
    return sum_evens, sum_odds

def _isbn_10_weighted_sum(isbn_array: List[int]) -> int:
    sum_digits = 0
    for index, digit in enumerate(isbn_array):
        sum_digits += (digit * (10 - index))
    return sum_digits

def _check_isbn_chars(isbn: str) -> bool:
    char_check_isbn = isbn[0:-1] if isbn[-1].upper() == "X" else isbn
    return True if char_check_isbn.isnumeric() else False

def _check_isbn_length(isbn: str) -> bool:
    return True if (len(isbn) == 13) or (len(isbn) == 10) else False

def _check_isbn_13_valid(isbn_array: List[int]) -> bool:
    sum_evens, sum_odds = _isbn_13_weighted_sum(isbn_array)
    return ((sum_evens + sum_odds) % 10) == 0

def _check_isbn_10_valid(isbn_array: List[int]) -> bool:
    sum_digits = _isbn_10_weighted_sum(isbn_array)
    return (sum_digits % 11) == 0

def _check_isbn_valid(isbn: str) -> bool:
    isbn_array = _cast_str_to_int_array(isbn)
    return _check_isbn_13_valid(isbn_array) if len(isbn) == 13 else _check_isbn_10_valid(isbn_array)

def _calc_isbn_13_check_digit(isbn_array: List[int]) -> int:
    sum_evens, sum_odds = _isbn_13_weighted_sum(isbn_array)  
    return (10 - ((sum_evens + sum_odds) % 10)) % 10

def _calc_isbn_10_check_digit(isbn_array: List[int]) -> int:
    sum_digits = _isbn_10_weighted_sum(isbn_array)
    return (11 - (sum_digits % 11))

def validate_isbn(isbn: str) -> Tuple[bool, str]:
    if not _check_isbn_chars(isbn):
        return False, "Invalid Character"

    if not _check_isbn_length(isbn):
        return False, "Invalid Length"

    if not _check_isbn_valid(isbn):
        return False, "Invalid ISBN"
    
    return True, ""

def convert_isbn_10_to_13(isbn: str) -> str:
    isbn_array = _cast_str_to_int_array(isbn)
    del isbn_array[-1]
    isbn_array = [9, 7, 8] + isbn_array
    isbn_array = isbn_array + [_calc_isbn_13_check_digit(isbn_array)]
    return _cast_int_array_to_str(isbn_array)

def convert_isbn_13_to_10(isbn: str) -> str:
    isbn_array = _cast_str_to_int_array(isbn)
    if isbn_array[0:3] != [9, 7, 8]:
        return None
    del isbn_array[-1]
    isbn_array = isbn_array[3:]
    isbn_array = isbn_array + [_calc_isbn_10_check_digit(isbn_array)]
    return _cast_int_array_to_str(isbn_array)
