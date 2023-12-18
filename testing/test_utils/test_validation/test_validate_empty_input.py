import pytest
from utils.validation import validate_empty_input


class TestEmptyInput:

    def check_empty_input(self, input_val, expected_val):
        val_received = validate_empty_input(input_val)
        assert val_received == expected_val

    def test_empty_input(self):
        self.check_empty_input('', True)

    def test_empty_input_negative(self):
        self.check_empty_input('notempty', False)
