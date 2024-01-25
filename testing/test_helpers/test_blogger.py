import pytest
from unittest.mock import patch, Mock, MagicMock

from helpers import blogger
from helpers.blogger import User, Blog, Comment, Database, prompts, GeneralLogger, Role, Flag, filepaths, take_input


class TestBlogger:
    @pytest.fixture
    def mock_user(self, mocker):
        mock_user_class = Mock(spec=User)
        _instance = mock_user_class.return_value
        mocker.patch('helpers.user.User', return_value=_instance)
        return mock_user_class()

    @pytest.fixture
    def mock_blog(self, mocker):
        Blog_m = Mock(spec=Blog)
        _instance = Blog_m.return_value
        mocker.patch('helpers.user.Blog', return_value=_instance)
        return Blog_m

    @pytest.fixture
    def mock_comment(self, mocker):
        Comment_m = Mock(spec=Comment)
        _instance = Comment_m.return_value
        mocker.patch('helpers.user.Comment', return_value=_instance)
        return Comment_m

    @pytest.fixture(autouse=True)
    def mock_logger(self, mocker):
        return mocker.patch('helpers.user.GeneralLogger')

    @pytest.fixture
    def mock_database(self, mocker):
        return mocker.patch('helpers.user.Database')

    @pytest.fixture
    def mock_validation(self, mocker):
        return mocker.patch('helpers.user.validation')

    def test_get_users_returns_list_of_users(self, mocker, mock_user):
        # Mock the database access to return predefined data
        mock_user = Mock(spec=User)
        _instance = mock_user.return_value
        mocker.patch('helpers.user.User', return_value=_instance)
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
        mocker.patch('helpers.user.validation.validate_password', return_value=True)
        mocker.patch('helpers.user.take_input', return_value='new_password')

        from helpers.blogger import Authentication
        mocker.patch.object(Authentication, 'hash_password', return_value='hashed_password')

        mock_user.user_role = 2
        blogger.change_password(mock_user)
        captured = capsys.readouterr()

        assert captured.out.rstrip() == prompts.SUCCESSFUL_PASSWORD_CHANGE
        mock_logger.info.assert_called()

    def test_change_password_invalid_first(self, capsys, mocker, mock_user, mock_logger):
        mocker.patch('helpers.user.validation.validate_password', return_value=False)
        mocker.patch('helpers.user.take_input', return_value='new_password')

        mock_user.user_role = 2
        from helpers.blogger import Authentication
        mocker.patch.object(Authentication, 'hash_password', return_value='hashed_password')

        with patch('helpers.user.validation.validate_password', side_effect=[False, True]):
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
            mocker.patch('helpers.user.User', return_value=mock_user)
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
        mocker.patch('helpers.user.User', return_value=mock_user)
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

    def test_view_blogs_by_user_or_tag_positive(self, capsys, mock_database, mock_blog):
        mock_database.get_items.return_value = [('TestBlog1', 'TestContent'), ('TestBlog2', 'TestContent')]

        blogger.view_blogs_by_user('dummy_user')
        blogger.view_blogs_by_tag_name('dummy_tag')

        capsys.readouterr()

        mock_blog_instance = mock_blog.return_value
        mock_blog_instance.details.assert_called()

    def test_view_blogs_by_user_not_found(self, capsys, mock_database):
        mock_database.get_items.return_value = []

        blogger.view_blogs_by_user('dummy_user')
        captured = capsys.readouterr()

        assert prompts.NO_BLOG_BY_USER.format('dummy_user') in captured.out

    def test_view_blogs_by_tag_not_found(self, capsys, mock_database):
        mock_database.get_items.return_value = []

        blogger.view_blogs_by_tag_name('dummy_tag')
        captured = capsys.readouterr()

        assert prompts.NO_BLOG_OF_TAG_NAME.format('dummy_tag') in captured.out

    def test_view_one_blog(self, capsys, mocker, monkeypatch, mock_blog, mock_database):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = [(101, 'Snowden', 'Content', 'Creator', 4, 'adventure', '2023-12-12')]

        mock_blog_instance = mock_blog.return_value

        mock_comment = Mock()
        mock_comment_instance = mock_comment.return_value
        mock_comment.get_details.return_value = True

        # alternative:  monkeypatch.setattr(mock_blog_instance, 'get_comments', lambda _: [(1, 'Comment1'), (2,
        # 'Comment2')])
        mocker.patch.object(mock_blog_instance, 'get_comments',
                            return_value=[mock_comment_instance, mock_comment_instance])
        result = blogger.view_one_blog()

        capsys.readouterr()

        assert result is True
        mock_blog_instance.details.assert_called()
        mock_comment_instance.details.assert_called()

    def test_view_one_blog_not_found(self, capsys, mocker, mock_database):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = None

        result = blogger.view_one_blog()

        captured = capsys.readouterr()

        assert prompts.BLOG_NOT_FOUND_NAME.format('test_title') in captured.out
        assert result == Flag.DOES_NOT_EXIST.value

    def test_create_blog(self, capsys, mocker, mock_database, mock_user, mock_blog):
        mocker.patch.object(take_input, 'get_blog_post_details', return_value=('test_title', 'test_content', 'test'))
        mock_database.get_item.return_value = False  # assuming this is a new entry
        blog_instance = mock_blog()
        blog_instance.add_content.return_value = True  # added the blog successfully

        mock_user.username = 'test_user'
        blogger.create_blog(mock_user)
        captured = capsys.readouterr()

        assert prompts.BLOG_ADDED.format('test_title') in captured.out

    def test_create_blog_negative(self, mocker, mock_user, capsys, mock_database):
        mocker.patch.object(take_input, 'get_blog_post_details', return_value=('test_title', 'test_content', 'test'))
        mock_database.get_item.return_value = True  # there's an existing entry by that name

        blogger.create_blog(mock_user)

        captured = capsys.readouterr()

        assert prompts.CHOOSE_ANOTHER_TITLE in captured.out

    @pytest.mark.parametrize("edited, expected_output", [
        (True, prompts.BLOG_EDITED.format('test_title')),
        (False, prompts.COULD_NOT_EDIT_BLOG.format('test_title'))
    ])
    def test_edit_blog(self, edited, expected_output, capsys, mocker, mock_user, mock_database, mock_blog):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mocker.patch.object(take_input, 'get_new_content', return_value='test_content')
        mock_database.get_item.return_value = [101, 'test_title', 'test_author', 'test_date']

        blog_instance = mock_blog()
        mocker.patch.object(blog_instance, 'set_blog_id')
        blog_instance.set_blog_id.return_value = True

        mocker.patch.object(blog_instance, 'edit_content', return_value=edited)

        blogger.edit_blog(mock_user)

        captured = capsys.readouterr()
        assert expected_output in captured.out

    def test_edit_blog_not_found(self, capsys, mocker, mock_user, mock_database):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = None

        mock_user.username = 'einstein'

        result = blogger.edit_blog(mock_user)

        captured = capsys.readouterr()

        assert result == Flag.DOES_NOT_EXIST.value
        assert prompts.BLOG_NOT_FOUND_BLOG_USER.format('test_title', mock_user.username) in captured.out

    @pytest.mark.parametrize("removed, expected_output", [
        (True, prompts.BLOG_REMOVED.format('test_title')),
        (False, prompts.COULD_NOT_REMOVE_BLOG)
    ])
    def test_remove_blog(self, removed, expected_output, capsys, mocker, mock_user, mock_database, mock_blog,
                         mock_logger):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = [101, 'test_title', 'test_author', 'test_date']

        blog_instance = mock_blog()

        mocker.patch.object(blog_instance, 'remove_content', return_value=removed)

        mock_user.username = 'snowden'
        blogger.remove_blog(mock_user)

        captured = capsys.readouterr()
        assert expected_output in captured.out

        if removed:
            mock_logger.info.assert_called_once()

    def test_remove_blog_not_found(self, capsys, mocker, mock_user, mock_database):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = None

        mock_user.username = 'einstein'

        result = blogger.remove_blog(mock_user)

        captured = capsys.readouterr()

        assert result == Flag.DOES_NOT_EXIST.value
        assert prompts.BLOG_NOT_FOUND_BLOG_USER.format('test_title', mock_user.username) in captured.out

    @pytest.mark.parametrize("removed, expected_output", [
        (True, prompts.BLOG_REMOVED.format('test_title')),
        (False, prompts.COULD_NOT_REMOVE_BLOG)
    ])
    def test_admin_remove_blog(self, capsys, removed, expected_output, mocker, mock_user, mock_database, mock_blog,
                               mock_logger):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = [101, 'test_title', 'test_author', 'test_date']

        blog_instance = mock_blog()

        mocker.patch.object(blog_instance, 'remove_content_by_title', return_value=removed)

        mock_user.username = 'snowden'
        mock_user.user_role = 1  # Admin role
        blogger.admin_remove_blog(mock_user)

        captured = capsys.readouterr()
        assert expected_output in captured.out

        if removed:
            mock_logger.info.assert_called_once()

    def test_admin_remove_blog_not_found(self, capsys, mocker, mock_user, mock_database):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = None

        mock_user.username = 'einstein'
        mock_user.user_role = 1

        result = blogger.admin_remove_blog(mock_user)

        captured = capsys.readouterr()

        assert result == Flag.DOES_NOT_EXIST.value
        assert prompts.BLOG_NOT_FOUND_NAME.format('test_title') in captured.out

    @pytest.mark.parametrize("upvoted, expected_output", [
        (True, prompts.UPVOTED_BLOG.format('test_title')),
        (False, prompts.COULD_NOT_UPVOTE_BLOG.format('test_title'))
    ])
    def test_upvote_blog(self, upvoted, expected_output, capsys, mocker, mock_user, mock_database, mock_blog,
                         mock_logger):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = [101, 'test_title', 'test_author', 'test_date']

        blog_instance = mock_blog()

        mocker.patch.object(blog_instance, 'upvote', return_value=upvoted)

        mock_user.username = 'snowden'
        blogger.upvote_blog(mock_user)

        captured = capsys.readouterr()
        assert expected_output in captured.out

    def test_upvote_blog_not_found(self, capsys, mocker, mock_user, mock_database):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = None

        mock_user.username = 'einstein'

        result = blogger.upvote_blog(mock_user)

        captured = capsys.readouterr()

        assert result == Flag.DOES_NOT_EXIST.value
        assert prompts.BLOG_NOT_FOUND_NAME.format('test_title') in captured.out

    @pytest.mark.parametrize("comment_added, expected_output", [
        (True, prompts.COMMENT_ADDED),
        (False, prompts.COMMENT_NOT_ADDED)
    ])
    def test_comment_on_blog(self, comment_added, expected_output, capsys, mocker, mock_database,
                             mock_user, mock_blog, mock_comment):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mocker.patch.object(take_input, 'get_comment', return_value='test_comment')
        mock_database.get_item.return_value = [101, 'test_title', 'test_author', 'test_date']

        blog_instance = mock_blog()
        blog_instance.set_blog_id.return_value = True

        comment_instance = mock_comment()
        mocker.patch.object(comment_instance, 'add_content', return_value=comment_added)
        # or: comment_instance.add_content.return_value = comment_added
        mock_user.user_role = 2
        mock_user.user_name = 'edward'

        blogger.comment_on_blog(mock_user)

        captured = capsys.readouterr()

        assert captured.out.strip() == expected_output

    def test_comment_on_blog_not_found(self, capsys, mocker, mock_user, mock_database):
        mocker.patch.object(take_input, 'get_title', return_value='test_title')
        mock_database.get_item.return_value = None

        mock_user.username = 'einstein'

        result = blogger.comment_on_blog(mock_user)

        captured = capsys.readouterr()

        assert result == Flag.DOES_NOT_EXIST.value
        assert prompts.BLOG_NOT_FOUND_NAME.format('test_title') in captured.out
