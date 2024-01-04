import pytest
from unittest.mock import Mock, patch
from src.views.admin import admin_choice_menu, admin_menu, prompts, remove_user_by_username


class TestAdminView:
    class User:
        def __init__(self, username, role, email):
            self.username = username
            self.role = role
            self.email = email

        def get_details(self):
            return {'username': self.username, 'role': self.role, 'email': self.email}

    @pytest.fixture
    def mock_user(self):
        user_class = Mock()
        _instance = user_class.return_value
        return _instance

    @pytest.fixture
    def mock_admin_menu(self, mocker):
        return mocker.patch('src.views.admin.admin_menu')

    @pytest.fixture
    def mock_blogger_menu(self, mocker):
        return mocker.patch('src.views.admin.blogger_menu')

    @pytest.mark.parametrize("choices", [('1', '2', '4', '3')])
    def test_admin_choice_menu(self, capsys, choices, monkeypatch, mock_user, mock_admin_menu, mock_blogger_menu):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        mock_admin_menu.return_value = True
        mock_blogger_menu.return_value = True

        admin_choice_menu(mock_user)
        captured = capsys.readouterr()

        if choice == '1':
            mock_admin_menu.assert_called()
        elif choice == '2':
            mock_blogger_menu.assert_called()
        elif choice == '4':
            assert captured == prompts.ENTER_VALID_CHOICE

        mock_admin_menu.assert_called()

    # def test_admin_choice_menu_2(self, mock_user):
    #     # Mock the input function
    #     with patch('builtins.input', side_effect=['1', '2', '3', 'invalid']):
    #         # Mock the admin_menu and blogger_menu functions
    #         with patch('src.views.admin.admin_menu') as mock_admin_menu, patch(
    #                 'src.views.admin.blogger_menu') as mock_blogger_menu:
    #             # Call the function to be tested
    #             admin_choice_menu(mock_user)
    #
    #     # Check if the functions are called as expected
    #     mock_admin_menu.assert_called_with(mock_user)
    #     mock_blogger_menu.assert_called_with(mock_user)

    @pytest.mark.parametrize("choices", [('1', '4', '5')])
    def test_admin_menu_choice_1_4(self, capsys, mock_user, monkeypatch, choices):
        choice = iter(choices)

        patch_admin_remove_blog = patch('src.views.admin.admin_remove_blog')
        mock_admin_remove_blog = patch_admin_remove_blog.start()

        patch_change_password = patch('src.views.admin.change_password')
        mock_change_password = patch_change_password.start()

        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        admin_menu(mock_user)

        mock_admin_remove_blog.assert_called_once()
        mock_change_password.assert_called_once()

    @pytest.mark.parametrize("choices", [('2', '5')])
    def test_admin_menu_choice_2(self, capsys, mock_user, monkeypatch, choices):
        choice = iter(choices)

        patch_get_users = patch('src.views.admin.get_users')
        mock_get_users = patch_get_users.start()

        mocked_users = [
            self.User(username='user1', role='1', email='user1@example.com'),
            self.User(username='user2', role='2', email='user2@example.com'),
        ]

        mock_get_users.return_value = mocked_users

        patch_change_password = patch('src.views.admin.change_password')
        patch_change_password.start()

        patch_display_users = patch('src.views.admin.display_users')
        mock_display_users = patch_display_users.start()

        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        mock_user.get_details.return_value = True

        admin_menu(mock_user)

        capsys.readouterr()

        mock_display_users.assert_called_once()

    @pytest.mark.parametrize("choices", [('3', 'test_user', '5')])
    def test_admin_menu_choice_3(self, capsys, mock_user, monkeypatch, choices):
        choice = iter(choices)

        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        patch_remove_user_by_username = patch('src.views.admin.remove_user_by_username')
        mock_remove_user_by_username = patch_remove_user_by_username.start()
        mock_remove_user_by_username.return_value = True

        admin_menu(mock_user)

        captured = capsys.readouterr()
        assert captured.out.strip() == prompts.USER_REMOVED
