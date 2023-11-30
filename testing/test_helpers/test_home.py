import pytest
from unittest.mock import patch, Mock
from src.helpers.home import Flag, prompts, signup, signin, filepaths


class TestHome:
    class TempUser:
        def __init__(self, username):
            self.username = username

    @pytest.fixture(autouse=True)
    def mock_take_input(self, mocker):
        return mocker.patch('src.helpers.home.take_input')

    @pytest.fixture
    def mock_authentication(self, mocker):
        return mocker.patch('src.helpers.home.Authentication')

    @pytest.fixture
    def mock_user(self, mocker):
        return mocker.patch('src.helpers.home.User')

    @pytest.fixture
    def mock_database(self, mocker):
        return mocker.patch('src.helpers.home.Database')

    @pytest.mark.parametrize("test_data", [
        (
                Flag.INVALID_USERNAME.value, Flag.ALREADY_EXISTS.value, Flag.INVALID_PASSWORD.value,
                Flag.INVALID_EMAIL.value, TempUser('snowden'),

        ),
    ])
    def test_home_signup_negative(self, monkeypatch, test_data, capsys, mock_take_input, mock_authentication):
        patch('builtins.print')

        user_status = iter(test_data)

        mock_take_input.get_user_details.return_value = [('snowden', 'password', 'email')]
        monkeypatch.setattr(mock_authentication, 'sign_up', lambda _: next(user_status))

        signup()
        captured = capsys.readouterr()

        line_obtained = captured.out.split('\n')
        assert line_obtained[-2] == prompts.USER_SIGNED_UP.format('snowden')

    @patch('builtins.print')
    @patch('src.helpers.home.take_input.get_user_details')
    @patch('src.helpers.home.Authentication.sign_up')
    @patch('src.helpers.home.GeneralLogger.info')
    def test_signup_successful(self, mock_info, mock_sign_up, mock_get_user_details, mock_print):
        mock_get_user_details.return_value = [{'username': 'test_user', 'password': 'test_password',
                                               'email': 'test@example.com'}]

        mock_sign_up.return_value = Mock(username='test_user')

        signup()

        mock_print.assert_called_with(prompts.USER_SIGNED_UP.format('test_user'))
        mock_get_user_details.assert_called_once()

        mock_sign_up.assert_called_once_with(
            {'username': 'test_user', 'password': 'test_password', 'email': 'test@example.com'}
        )
        mock_info.assert_called_with(prompts.USER_SIGNED_UP.format('test_user'), filepaths.USER_LOG_FILE)

    @pytest.mark.parametrize("user_role", [1, 2])
    def test_home_signin_positive(self, user_role, capsys, mock_take_input, mock_authentication,
                                  mock_user, mock_database):
        patch('builtins.print')

        mock_take_input.get_username_password.return_value = ('snowden', 'password')
        mock_authentication.sign_in.return_value = 'snowden'

        _instance = mock_user.return_value
        _instance.set_user_id.return_value = True
        _instance.user_role = user_role

        # mock the admin and blogger menu call

        patch_admin_menu = patch('src.helpers.home.admin_choice_menu', return_value=True)
        patch_admin_menu.start()
        patch_blogger_menu = patch('src.helpers.home.blogger_menu', return_value=True)
        patch_blogger_menu.start()

        signin()

        captured = capsys.readouterr()

        line_obtained = captured.out.split('\n')
        assert line_obtained[-2] == prompts.USER_LOGGED_IN.format('snowden')
        patch_admin_menu.stop()
        patch_blogger_menu.stop()

    @pytest.mark.parametrize("test_data", [
        (
                Flag.INVALID_USERNAME.value, Flag.DOES_NOT_EXIST.value, 'snowden',
        ),
    ])
    def test_home_signin_negative(self, monkeypatch, test_data, capsys, mock_take_input, mock_authentication,
                                  mock_user, mock_database):
        patch('builtins.print')

        user_status = iter(test_data)

        mock_take_input.get_username_password.return_value =[{'snowden', 'password'}]
        monkeypatch.setattr(mock_authentication, 'sign_in', lambda _: next(user_status))
        _instance = mock_user.return_value
        _instance.set_user_id.return_value = True

        # mock the admin and blogger menu call

        patch_admin_menu = patch('src.helpers.home.admin_choice_menu', return_value=True)
        patch_admin_menu.start()
        patch_blogger_menu = patch('src.helpers.home.blogger_menu', return_value=True)
        patch_blogger_menu.start()

        signin()
        captured = capsys.readouterr()

        line_obtained = captured.out.split('\n')
        assert line_obtained[-2] == prompts.USER_LOGGED_IN.format('snowden')
        patch_admin_menu.stop()
        patch_blogger_menu.stop()
