import pytest
from src.controllers.authentication import Authentication


class TestSignIn:

    @pytest.fixture(autouse=True)
    def setup(self):
        print("\nSetting up the sign in tests")

    def check_sign_in(self, expected_val, *args):
        val_received = Authentication.sign_in(*args)
        assert val_received == expected_val

    def test_empty_input(self):
        self.check_sign_in(-1, '', '')

    def test_user_does_not_exist(self):
        self.check_sign_in(-1, 'boogeyman', 'Random#2121')

    def test_user_wrong_password(self):
        self.check_sign_in(False, 'snow123', 'WrongPassword123')

    def test_user_right_credentials(self):
        self.check_sign_in('temp9', 'temp9', 'Temp123#123')
