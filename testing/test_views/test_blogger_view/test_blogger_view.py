import pytest
from unittest.mock import patch, Mock
from src.helpers.blogger import take_input
from src.views import blogger
from src.views.blogger import blogger_menu


class TestBloggerView:
    @pytest.fixture
    def mock_take_input(self, mocker):
        return mocker.patch('src.views.blogger.take_input')

    @pytest.fixture(autouse=True)
    def mock_user(self):
        return Mock(username='test_user')

    @pytest.mark.parametrize('choices', [('1', '11')])
    def test_choice_1(self, choices, monkeypatch, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        with patch('src.views.blogger.view_blogs') as mock_view_blogs:
            mock_view_blogs.return_value = True  # only for testing
            blogger_menu(mock_user)

        mock_view_blogs.assert_called()

    @pytest.mark.parametrize('choices', [('2', '11')])
    def test_choice_2(self, choices, monkeypatch, mock_take_input, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        mock_take_input.get_user_for_blog.return_value = 'test_user'

        with patch('src.views.blogger.view_blogs_by_user') as mock_view_blogs_by_user:
            mock_view_blogs_by_user.return_value = True
            blogger_menu(mock_user)

        mock_view_blogs_by_user.assert_called()
