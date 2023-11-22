import pytest
from src.controllers.authentication import Authentication


class TestSignUp:
    @pytest.fixture()
    def setup(self):
        print("\nSetting up the sign up tests")

    def check_sign_up(self, expected_val, *args):
        val_received = Authentication.sign_up(*args)
        assert val_received == expected_val

    def test_empty_input(self):
        self.check_sign_up(-4, "", "", "")

    def test_invalid_username(self):
        self.check_sign_up(-4, "%%&&@!", "testmail@gmail.com", "Random123#123")

    def test_weak_password(self):
        self.check_sign_up(-3, "valid123", "testmail@gmail.com", "1231")
