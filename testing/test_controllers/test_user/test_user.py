import pytest
from models.user import User, Sql


class TestUser:
    @pytest.fixture(autouse=True)
    def mock_database(self, mocker):
        return mocker.patch('controllers.user.Database')

    @pytest.fixture(autouse=True)
    def mock_logger(self, mocker):
        return mocker.patch('controllers.user.GeneralLogger')

    @pytest.fixture
    def user_info_start(self):
        return (
            'Test User',
            "Test Password",
            "Test Role",
            "Test Email",
            "2023-11-27"
        )

    @pytest.fixture
    def user_instance(self, user_info_start):
        return User(*user_info_start)

    def test_get_details(self, user_instance):
        expected_details = {
            'username': 'Test User',
            'role': 'Test Role',
            'email': 'Test Email',
            'registration_date': '2023-11-27',
        }

        result = user_instance.get_details()

        assert result == expected_details

    def test_set_user_id(self, user_instance):
        user_id = 22
        user_instance.set_user_id(user_id)

        assert user_instance.user_id == user_id

    def test_add_success(self, mock_logger, mock_database, user_instance):
        user_instance.user_id = 22
        mock_database.insert_item.return_value = 42  # Simulate insert_item result

        result = user_instance.add()

        assert result is True
        assert user_instance.user_id == 42
        mock_database.insert_item.assert_called_once_with(Sql.INSERT_USER.value, (
            "Test User",
            "Test Password",
            "Test Role",
            "Test Email",
            "2023-11-27",
        ))
        mock_logger.error.assert_not_called()

    def test_add_failure(self, mock_logger, mock_database, user_instance):
        user_instance.user_id = None
        mock_database.insert_item.side_effect = Exception("Test error")

        result = user_instance.add()

        assert result is False
        assert user_instance.user_id is None
        mock_database.insert_item.assert_called_once_with(Sql.INSERT_USER.value, (
            "Test User",
            "Test Password",
            "Test Role",
            "Test Email",
            "2023-11-27",
        ))

        mock_logger.error.assert_called_once()

    def test_remove_user_by_username_success(self, mock_logger, mock_database, user_instance):
        result = user_instance.remove_user_by_username()

        assert result is True
        mock_database.remove_item.assert_called_once_with(Sql.REMOVE_USER_BY_USERNAME.value, ("Test User",))
        mock_logger.error.assert_not_called()

    def test_remove_user_by_username_failure(self, mock_logger, mock_database, user_instance):
        mock_database.remove_item.side_effect = Exception("Test error")
        result = user_instance.remove_user_by_username()

        assert result is False
        mock_database.remove_item.assert_called_once_with(Sql.REMOVE_USER_BY_USERNAME.value, ("Test User",))
        mock_logger.error.assert_called_once()

    def test_change_password_success(self, mock_logger, mock_database, user_instance):
        result = user_instance.change_password("new_password")

        assert result is True
        mock_database.insert_item.assert_called_once_with(Sql.UPDATE_PASSWORD.value, ("new_password", "Test User"))
        mock_logger.error.assert_not_called()

    def test_change_password_failure(self, mock_logger, mock_database, user_instance):
        mock_database.insert_item.side_effect = Exception("Test error")
        result = user_instance.change_password("new_password")

        assert result is False
        mock_database.insert_item.assert_called_once_with(Sql.UPDATE_PASSWORD.value, ("new_password", "Test User"))
        mock_logger.error.assert_called_once()