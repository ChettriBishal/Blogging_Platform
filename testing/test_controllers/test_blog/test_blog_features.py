import pytest
from unittest.mock import patch
from src.controllers.blog import Blog, Comment, Database, Sql, GeneralLogger, filepaths
from src.config import prompts


class TestBlog:
    @pytest.fixture(autouse=True)
    def mock_database(self, mocker):
        return mocker.patch('src.controllers.blog.Database')

    @pytest.fixture(autouse=True)
    def mock_logger(self, mocker):
        return mocker.patch('src.controllers.blog.GeneralLogger')

    @pytest.fixture
    def Blog(self, mocker):
        return mocker.patch('src.controllers.blog.Blog')

    @pytest.fixture(autouse=True)
    def blog_info(self):
        return (
            "Test Title",
            "Test Content",
            "Test Creator",
            0,
            "Test Tag",
            "2023-11-25",
        )

    @pytest.fixture
    def blog_instance(self, blog_info):
        return Blog(blog_info)

    def test_add_content_positive(self, mock_database, mock_logger, blog_instance, blog_info):
        mock_database.insert_item.return_value = 1

        result = blog_instance.add_content()

        assert (result is True)

        assert blog_instance.blog_id == 1
        mock_database.insert_item.assert_called_once_with(Sql.INSERT_BLOG.value, blog_info)
        mock_logger.error.assert_not_called()

    def test_add_content_negative(self, mock_database, mock_logger, blog_instance, blog_info):
        mock_database.insert_item.return_value = None

        mock_database.insert_item.side_effect = Exception("Test error")

        result = blog_instance.add_content()

        assert (result is not 1)

        assert not (blog_instance.blog_id == 1)
        mock_database.insert_item.assert_called_once_with(Sql.INSERT_BLOG.value, blog_info)
        mock_logger.error.assert_called_once()

    def test_edit_content_positive(self, blog_instance, mock_database, mock_logger):
        blog_instance.blog_id = 42  # Simulating an existing blog ID

        result = blog_instance.edit_content("New Test Content")

        assert (result is True)
        mock_database.get_item.assert_not_called()
        mock_database.query_with_params.assert_called_once_with(Sql.EDIT_BLOG.value, ("New Test Content", 42,))
        mock_logger.error.assert_not_called()

    def test_edit_content_negative(self, blog_instance, mock_database, mock_logger):
        blog_instance.blog_id = 42  # Simulating an existing blog ID

        mock_database.query_with_params.side_effect = Exception("Test Error")
        result = blog_instance.edit_content("New Test Content")

        assert (result is None)
        mock_database.get_item.assert_not_called()
        mock_database.query_with_params.assert_called_once_with(Sql.EDIT_BLOG.value, ("New Test Content", 42,))
        mock_logger.error.assert_called_once()

    @patch('src.controllers.blog.Blog.remove_comments')
    def test_remove_content_positive(self, monkeypatch, blog_instance, mock_database, mock_logger):
        blog_instance.blog_id = 42
        blog_instance.remove_comments.return_value = True
        result = blog_instance.remove_content()

        assert (result is True)
        mock_database.get_item.assert_not_called()
        blog_instance.remove_comments.assert_called_once()
        mock_database.remove_item.assert_called_once_with(Sql.REMOVE_BLOG_BY_ID.value, (42,))
        mock_logger.error.assert_not_called()

        pass

    @patch('src.controllers.blog.Blog.remove_comments')
    def test_remove_content_negative(self, monkeypatch, blog_instance, mock_database, mock_logger):
        blog_instance.blog_id = 42
        blog_instance.remove_comments.side_effect = Exception("Test Error")
        result = blog_instance.remove_content()

        assert (result is None)
        mock_database.get_item.assert_not_called()
        blog_instance.remove_comments.assert_called_once()
        mock_database.remove_item.assert_not_called()
        mock_logger.error.assert_called_once()

    def test_upvote_blog_positive(self, blog_instance, mock_database):
        blog_instance.blog_id = 11
        mock_database.get_item.return_value = None  # there's no record of upvote for user_id
        mock_database.query_with_params.side_effect = [(True,), (True,)]

        result = blog_instance.upvote(user_id=22)

        assert (result is True)
        assert blog_instance.upvotes == 1
        mock_database.get_item.assert_called_once_with(Sql.CHECK_BLOG_UPVOTE.value, (22, 11))
        mock_database.query_with_params.assert_called()

    def test_upvote_blog_negative(self, blog_instance, mock_database):
        blog_instance.blog_id = 11
        mock_database.get_item.return_value = True  # the user has already upvoted

        result = blog_instance.upvote(user_id=22)

        assert (result is False)
        assert (blog_instance.upvotes == 0)
        mock_database.get_item.assert_called_once_with(Sql.CHECK_BLOG_UPVOTE.value, (22, 11))
        mock_database.query_with_params.assert_not_called()

    def test_details(self, blog_instance):
        result = blog_instance.details()
        expected_details = prompts.BLOG_DETAILS.format(
            "Test Title", "Test Creator", "Test Tag", "2023-11-25", "Test Content", 0
        )

        assert (result == expected_details)

    def test_get_comments_positive(self, mock_database, blog_instance):
        blog_instance.blog_id = 22
        mock_database.get_items.return_value = [
            (11, 22, 'Test Content1', 'user1', 2, '2023-12-01'),
            (33, 22, 'Test Content2', 'user5', 5, '2023-11-01')
        ]

        result = blog_instance.get_comments()

        assert len(result) == 2
        assert all(isinstance(comment, Comment) for comment in result)

        mock_database.get_items.assert_called_once_with(Sql.GET_COMMENT_BY_BLOG_ID.value, (22,))

    def test_get_comments_negative(self, mock_database, blog_instance):
        blog_instance.blog_id = 22
        mock_database.get_items.return_value = None

        result = blog_instance.get_comments()

        assert (result is None)

        mock_database.get_items.assert_called_once_with(Sql.GET_COMMENT_BY_BLOG_ID.value, (22,))

    def test_remove_comments_positive(self):
        pass

    def test_remove_comments_negative(self):
        pass

    def test_remove_content_by_title_positive(self):
        pass

    def test_remove_content_by_title_negative(self):
        pass
