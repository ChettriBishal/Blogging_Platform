import pytest

from src.utils.validation import validate_email


class TestEmail:
    def check_email(self, input_val, expected_val):
        matched_or_not = validate_email(input_val)
        assert bool(matched_or_not) == expected_val

    def test_empty_input(self):
        self.check_email('', False)

    def test_invalid_input(self):
        self.check_email('2##12', False)
        self.check_email('invalid@', False)
        self.check_email('invalid@gmail.', False)

    def test_number_input(self):
        self.check_email('1231231', False)

    @pytest.mark.parametrize("email", ['bis@gmail.com', 'edward1snowden@gmail.com'])
    def test_valid_input(self, email):
        self.check_email(email, True)
