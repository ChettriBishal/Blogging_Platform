import pytest
from src.controllers.authentication import Authentication


class TestSignIn:

    @pytest.fixture()
    def setup(self):
        print("\nSetting up the sign in tests")

    def check_sign_in(self, expected_val, *args):
        val_received = Authentication.sign_in(*args)
        assert val_received == expected_val

    @pytest.mark.usefixtures("setup")
    def test_empty_input(self):
        self.check_sign_in(-4, '', '')

    @pytest.mark.usefixtures("setup")
    def test_user_does_not_exist(self):
        self.check_sign_in(-1, 'boogeyman', 'Random#2121')

    @pytest.mark.usefixtures("setup")
    def test_user_wrong_password(self):
        self.check_sign_in(False, 'snow123', 'WrongPassword123')
