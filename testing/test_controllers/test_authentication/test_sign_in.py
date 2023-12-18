import pytest
from controllers.authentication import Authentication
from unittest.mock import patch
from config.flags import Flag


class TestSignIn:

    @pytest.fixture(autouse=True)
    def setup(self):
        print("\nSetting up the sign in tests")

    @pytest.fixture
    def mock_database(self, mocker):
        with patch('controllers.authentication.Database') as mock_db:
            yield mock_db
        # return mocker.patch('controllers.authentication.Database')

    def check_sign_in(self, expected_val, *args):
        val_received = Authentication.sign_in(*args)
        assert val_received == expected_val

    def test_empty_input(self):
        self.check_sign_in(Flag.DOES_NOT_EXIST.value, '', '')

    def test_invalid_username(self, mocker):
        mocker.patch('controllers.authentication.validation.validate_username', return_value=None)
        self.check_sign_in(Flag.INVALID_USERNAME.value, 'invalid_username', 'some_password')

    def test_sign_in_successful(self, mocker, mock_database):
        mocker.patch('controllers.authentication.validation.validate_username', return_value=True)

        # mock_database.get_item.return_value = True
        # mocker.patch('controllers.authentication.Database.get_item', side_effect=[True, 'hashed_password'])

        mock_database.get_item.side_effect = [
            True,
            ('hashed_password',)
        ]

        mocker.patch.object(Authentication, '_check_password', return_value=True)

        result = Authentication.sign_in('temp9', 'hashed_password')

        assert result == 'temp9'
        mock_database.get_item.assert_called()

    def test_sign_in_failed(self, mocker, mock_database):
        mocker.patch('controllers.authentication.validation.validate_username', return_value=True)

        # mock_database.get_item.return_value = True
        # mocker.patch('controllers.authentication.Database.get_item', side_effect=[True, 'hashed_password'])

        mock_database.get_item.side_effect = [
            True,
            ('hashed_password',)
        ]

        mocker.patch.object(Authentication, '_check_password', return_value=False)

        result = Authentication.sign_in('temp9', 'bad_password')

        assert not (result == 'temp9')
        mock_database.get_item.assert_called()
