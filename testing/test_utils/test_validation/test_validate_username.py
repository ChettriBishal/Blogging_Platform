import pytest

from utils.validation import validate_username


class TestUsername:
    def check_username(self, input_val, expected_val):
        val_received = validate_username(input_val)
        assert val_received == expected_val

    def test_empty_input(self):
        self.check_username('', False)

    def test_invalid_input(self):
        self.check_username('2##12', False)
        self.check_username('123@user', False)
        self.check_username('user.ok', False)

    def test_number_input(self):
        self.check_username('1231231', False)

    @pytest.mark.parametrize("username, result",
                             [
                                 ("bishal", True),
                                 ("snow123", True),
                                 ("test222", True),
                                 ("_test12", True),
                                 ("_test_", True),
                                 ("_test_1_2", True)
                             ])
    def test_valid_input(self, username, result):
        self.check_username(username, result)
