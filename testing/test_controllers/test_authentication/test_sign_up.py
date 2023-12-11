import pytest
from unittest.mock import patch, Mock
from src.config.flags import Flag
from src.controllers.authentication import Authentication, User


class TestSignUp:
    @pytest.fixture
    def mock_database(self, mocker):
        with patch('src.controllers.authentication.Database') as mock_db:
            yield mock_db
        # return mocker.patch('src.controllers.authentication.Database')

    @pytest.fixture
    def mock_validation(self, mocker):
        with patch('controllers.authentication.validation') as mock_validation:
            yield mock_validation
        # return mocker.patch('controllers.authentication.validation')

    def check_sign_up(self, expected_val, *args):
        val_received = Authentication.sign_up(*args)
        assert val_received == expected_val

    def test_empty_input(self):
        self.check_sign_up(-4, "", "", "")

    def test_invalid_username(self, mocker):
        mocker.patch('controllers.authentication.validation.validate_username', return_value=None)
        result = Authentication.sign_in('invalid_username', 'some_password')

        assert result == Flag.INVALID_USERNAME.value

    def test_weak_password(self):
        self.check_sign_up(-3, "random123", "1231", "testmail@gmail.com")

    @pytest.mark.parametrize("username,password,email", [("onemore123", "Random123#123", "testing@gmail.com")])
    def test_sign_up_successful(self, monkeypatch, mock_database, mock_validation, username, password, email):
        mock_user = Mock(spec=User)
        _instance = mock_user.return_value
        mock_database.get_item.return_value = False
        monkeypatch.setattr(mock_user, 'add', lambda: True)

        with patch('src.controllers.authentication.User', return_value=_instance):
            res = Authentication.sign_up(username, password, email)

        assert res == _instance
        mock_database.get_item.assert_called_once()

    @pytest.mark.parametrize("username,password,email", [("##", "Random123#123", "testing@gmail.com")])
    def test_sign_up_failed(self, monkeypatch, mock_database, username, password, email):
        mock_user = Mock(spec=User)
        _instance = mock_user.return_value

        mock_database.get_item.return_value = False

        monkeypatch.setattr(mock_user, 'add', lambda: False)

        with patch('src.controllers.authentication.User', return_value=_instance):
            res = Authentication.sign_up(username, password, email)

        assert not (res == _instance)
        mock_database.get_item.assert_called_once()
