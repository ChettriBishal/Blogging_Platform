import pytest

from utils.validation import validate_password


class TestPassword:
    def check_password(self, input_val, expected_val):
        matched_or_not = validate_password(input_val)
        assert bool(matched_or_not) == expected_val

    def test_empty_input(self):
        self.check_password('', False)

    def test_invalid_text(self):
        self.check_password('2##12', False)

    def test_number_input(self):
        self.check_password('1231231', False)

    @pytest.mark.parametrize("password", ['Random123#123', '12312@!@!@gGH'])
    def test_valid_input(self, password):
        self.check_password(password, True)
