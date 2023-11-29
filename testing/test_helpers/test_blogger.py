import pytest
from unittest.mock import patch, Mock

from src.helpers import blogger
from src.helpers.blogger import User, Blog, Database, prompts, GeneralLogger, Role, Flag, filepaths


class TestBlogger:
    @pytest.fixture
    def mock_user(self, mocker):
        mock_user_class = Mock(spec=User)
        _instance = mock_user_class.return_value
        mocker.patch('src.helpers.blogger.User', return_value=_instance)
        return mock_user_class()

    @pytest.fixture
    def mock_blog(self, mocker):
        Blog_m = Mock(spec=Blog)
        _instance = Blog_m.return_value
        mocker.patch('src.helpers.blogger.Blog', return_value= _instance)
        return Blog_m

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
        assert users is None
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

    def test_change_password_invalid_first(self, capsys, mocker, mock_user, mock_logger):
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

    def test_display_users(self, capsys):
        pass

    @pytest.mark.parametrize("user_status, expected_output, expected_return", [
        (None, "", False),  # User not found
        ((1, 'test_user_2', 'password', Role.BLOGGER.value, 'test_mail_2', '2023-11-08'), "", True),
    ])
    def test_remove_user_by_username_empty_and_blogger(self, mocker, mock_user, mock_logger, user_status,
                                                       expected_output,
                                                       expected_return):
        mocker.patch.object(Database, 'get_item', return_value=user_status)

        mocker.patch.object(GeneralLogger, 'info')

        if user_status:
            mock_user.user_role = user_status[3]
            mocker.patch('src.helpers.blogger.User', return_value=mock_user)
            mocker.patch.object(mock_user, 'remove_user_by_username', return_value=True)

            result = blogger.remove_user_by_username('test_user_2')

            assert (result == expected_return)

            if result:
                mock_logger.info.assert_called_once_with(prompts.USER_WITH_USERNAME_REMOVED.format('test_user_2'),
                                                         filepaths.USER_LOG_FILE)

        else:
            result = blogger.remove_user_by_username('test_user')
            assert result is False

    @pytest.mark.parametrize("user_status, expected_output, expected_return", [
        ((1, 'test_user_1', 'password', Role.ADMIN.value, 'test_mail', '2023-11-09'),
         prompts.ADMIN_CANT_BE_REMOVED + '\n', Flag.INVALID_OPERATION.value),
    ])
    def test_remove_user_by_username_admin(self, capsys, mocker, mock_user, mock_logger, user_status, expected_output,
                                           expected_return):
        mocker.patch.object(Database, 'get_item', return_value=user_status)

        mocker.patch.object(GeneralLogger, 'info')

        mock_user.user_role = user_status[3]
        mocker.patch('src.helpers.blogger.User', return_value=mock_user)
        mocker.patch.object(mock_user, 'remove_user_by_username', return_value=True)

        result = blogger.remove_user_by_username('test_user_2')
        captured = capsys.readouterr()

        assert captured.out == expected_output

        assert (result == expected_return)

    def test_remove_user_by_username_exception(self, mock_database, mock_logger):
        mock_database.get_item.side_effect = Exception("Something went wrong")

        result = blogger.remove_user_by_username('bishal')

        assert result is False
        mock_logger.error.assert_called_once()



    def test_view_blogs_1(self, mock_database):

        pass

    def test_view_blogs(self, capsys, mocker, mock_blog):
        mocker.patch.object(Database, 'get_items', return_value=[(1, 'Blog Title', 'Blog Content')])

        blogger.view_blogs()

        # Capture the printed output
        capsys.readouterr()

        mock_blog_instance = mock_blog.return_value
        mock_blog_instance.details.assert_called_once()

    def test_view_blogs_negative(self, capsys, mock_database):
        mock_database.get_items.return_value = None

        blogger.view_blogs()
        captured = capsys.readouterr()

        assert prompts.BLOGS_NOT_FOUND in captured.out

