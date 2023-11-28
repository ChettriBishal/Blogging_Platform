import pytest
from unittest.mock import patch, Mock

from src.helpers import blogger
from src.helpers.blogger import User, Database, prompts


class TestBlogger:
    @pytest.fixture
    def mock_user(self, mocker):
        mock_user_class = Mock(spec=User)
        _instance = mock_user_class.return_value
        mocker.patch('src.helpers.blogger.User', return_value=_instance)
        return mock_user_class()

    @pytest.fixture(autouse=True)
    def mock_logger(self, mocker):
        return mocker.patch('src.helpers.blogger.GeneralLogger')

    @pytest.fixture
    def mock_database(self, mocker):
        return mocker.patch('src.helpers.blogger.Database')

    @pytest.fixture
    def mock_validation(self, mocker):
        return mocker.patch('src.helpers.blogger.validation')

    def test_get_users_returns_list_of_users(self, mocker, mock_user):
        # Mock the database access to return predefined data
        mock_user = Mock(spec=User)
        _instance = mock_user.return_value
        mocker.patch('src.helpers.blogger.User', return_value=_instance)
        mock_user.user_role = 1

        mocker.patch.object(Database, 'get_items', return_value=[(1, 'Edward', 'Snowden'), (2, 'Jane', 'Doe')])

        users = blogger.get_users(mock_user)

        assert len(users) == 2
        assert users[0] == _instance
        assert users[1] == _instance

    def test_get_users_exception_handled(self, mock_database, mock_user, mock_logger):
        mock_database.get_items.side_effect = PermissionError('Permission denied')
        mock_user.user_role = 1

        users = blogger.get_users(mock_user)
        mock_logger.info.assert_called()

    def test_change_password_valid(self, capsys, mocker, mock_user, mock_logger):
        mocker.patch('src.helpers.blogger.validation.validate_password', return_value=True)
        mocker.patch('src.helpers.blogger.take_input', return_value='new_password')

        from src.helpers.blogger import Authentication
        mocker.patch.object(Authentication, 'hash_password', return_value='hashed_password')

        mock_user.user_role = 2
        blogger.change_password(mock_user)
        captured = capsys.readouterr()

        assert captured.out.rstrip() == prompts.SUCCESSFUL_PASSWORD_CHANGE
        mock_logger.info.assert_called()

    def test_change_password_invalid(self, capsys, mocker, mock_user, mock_logger):
        mocker.patch('src.helpers.blogger.validation.validate_password', return_value=False)
        mocker.patch('src.helpers.blogger.take_input', return_value='new_password')

        mock_user.user_role = 2
        from src.helpers.blogger import Authentication
        mocker.patch.object(Authentication, 'hash_password', return_value='hashed_password')

        with patch('src.helpers.blogger.validation.validate_password', side_effect=[False, True]):
            blogger.change_password(mock_user)
            captured = capsys.readouterr()

            assert captured.out.strip() == (
                        prompts.ENTER_STRONG_PASSWORD.strip() + '\n' * 2 +
                        prompts.SUCCESSFUL_PASSWORD_CHANGE.strip()
            )
            mock_logger.info.assert_called()
