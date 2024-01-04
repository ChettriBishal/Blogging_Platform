import pytest
from unittest.mock import patch, Mock
from src.views.blogger import blogger_menu
from src.views.blogger import prompts


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

        mock_view_blogs.assert_called_once()

    @pytest.mark.parametrize('choices', [('2', '11')])
    def test_choice_2(self, choices, monkeypatch, mock_take_input, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        mock_take_input.get_user_for_blog.return_value = 'test_user'

        with patch('src.views.blogger.view_blogs_by_user') as mock_view_blogs_by_user:
            mock_view_blogs_by_user.return_value = True
            blogger_menu(mock_user)

        mock_view_blogs_by_user.assert_called_once()

    @pytest.mark.parametrize('choices', [('3', '11')])
    def test_choice_3(self, choices, monkeypatch, mock_take_input, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        mock_take_input.get_tag_name.return_value = 'test_tag'

        with patch('src.views.blogger.view_blogs_by_tag_name') as mock_view_blogs_by_tag_name:
            mock_view_blogs_by_tag_name.return_value = True
            blogger_menu(mock_user)

        mock_view_blogs_by_tag_name.assert_called_once()

    @pytest.mark.parametrize('choices', [('4', '11')])
    def test_choice_4(self, choices, monkeypatch, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        with patch('src.views.blogger.view_one_blog') as mock_view_one_blog:
            mock_view_one_blog.return_value = True
            blogger_menu(mock_user)

        mock_view_one_blog.assert_called_once()

    @pytest.mark.parametrize('choices', [('5', '11')])
    def test_choice_5(self, choices, monkeypatch, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        with patch('src.views.blogger.create_blog') as mock_create_blog:
            mock_create_blog.return_value = True
            blogger_menu(mock_user)

        mock_create_blog.assert_called_once()

    @pytest.mark.parametrize('choices', [('6', '11')])
    def test_choice_6(self, choices, monkeypatch, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        with patch('src.views.blogger.edit_blog') as edit_blog:
            edit_blog.return_value = True
            blogger_menu(mock_user)

        edit_blog.assert_called_once()

    @pytest.mark.parametrize('choices', [('7', '11')])
    def test_choice_7(self, choices, monkeypatch, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        with patch('src.views.blogger.remove_blog') as mock_remove_blog:
            mock_remove_blog.return_value = True
            blogger_menu(mock_user)

        mock_remove_blog.assert_called_once()

    @pytest.mark.parametrize('choices', [('8', '11')])
    def test_choice_8(self, choices, monkeypatch, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        with patch('src.views.blogger.upvote_blog') as mock_upvote_blog:
            mock_upvote_blog.return_value = True
            blogger_menu(mock_user)

        mock_upvote_blog.assert_called_once()

    @pytest.mark.parametrize('choices', [('9', '11')])
    def test_choice_9(self, choices, monkeypatch, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        with patch('src.views.blogger.comment_on_blog') as mock_comment_on_blog:
            mock_comment_on_blog.return_value = True
            blogger_menu(mock_user)

        mock_comment_on_blog.assert_called_once()

    @pytest.mark.parametrize('choices', [('10', '11')])
    def test_choice_10(self, choices, monkeypatch, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        with patch('src.views.blogger.change_password') as mock_change_password:
            mock_change_password.return_value = True
            blogger_menu(mock_user)

        mock_change_password.assert_called_once()

    @pytest.mark.parametrize('choices', [('13', '11')])
    def test_choice_10(self, capsys, choices, monkeypatch, mock_user):
        choice = iter(choices)
        monkeypatch.setattr('builtins.input', lambda _: next(choice))

        blogger_menu(mock_user)

        captured = capsys.readouterr()
        assert captured.out.strip() in prompts.ENTER_VALID_CHOICE



