import pytest
import re

from src.utils.validation import validate_username


def check_username(input_val, expected_val):
    val_received = validate_username(input_val)
    assert val_received == expected_val


def test_empty_input():
    check_username('', False)


def test_invalid_text():
    check_username('2##12', False)


def test_number_input():
    check_username('1231231', False)


@pytest.mark.parametrize("username, result",
                         [
                             ("bishal", True),
                             ("snow123", True),
                             ("test222", True),
                             ("_test12", True),
                             ("_test_", True),
                             ("_test_1_2", True)
                         ])
def test_valid_input(username, result):
    print(f"testing `{username}`")
    check_username(username, result)
