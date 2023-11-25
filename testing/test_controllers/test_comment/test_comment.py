import pytest
from unittest.mock import patch, call
from src.controllers.comment import Comment, Sql
from src.config import prompts


class TestComment:
    @pytest.fixture(autouse=True)
    def mock_database(self, mocker):
        return mocker.patch('src.controllers.comment.Database')

    @pytest.fixture(autouse=True)
    def mock_logger(self, mocker):
        return mocker.patch('src.controllers.comment.GeneralLogger')

    @pytest.fixture
    def Comment(self, mocker):
        return mocker.patch('src.controllers.comment.Comment')

    @pytest.fixture
    def comment_info_start(self):
        return (
            1,  # blog_id
            "Test Content",
            "Test Creator",
            0,
            "2023-11-25",
        )

    @pytest.fixture
    def comment_instance(self, comment_info_start):
        return Comment(comment_info_start)

    def test_add_content(self, mock_database, mock_logger, comment_instance):
        mock_database.insert_item.return_value = 42  # Simulate insert_item result

        result = comment_instance.add_content()

        assert result is True
        assert comment_instance.comment_id == 42
        mock_database.insert_item.assert_called()

        mock_logger.error.assert_not_called()

    def test_add_content_negative(self, mock_database, mock_logger, comment_instance):
        mock_database.insert_item.return_value = None  # Simulate insert_item result

        mock_database.insert_item.side_effect = Exception("Test Error")
        result = comment_instance.add_content()

        assert not result
        assert comment_instance.comment_id is None
        mock_database.insert_item.assert_called()

        mock_logger.error.assert_called()

    def test_remove_content(self, monkeypatch, comment_instance, comment_info_start, mock_logger, mock_database):
        mock_database.get_item.return_value = 42
        comment_instance.comment_id = 42

        result = comment_instance.remove_content()

        assert result is True
        mock_database.get_item.assert_called_once_with(Sql.GET_COMMENT_ID.value, (1, "Test Creator"))
        mock_database.remove_item.assert_called_once_with(Sql.REMOVE_COMMENT_BY_ID.value, (42,))
        mock_logger.error.assert_not_called()

    def test_remove_content_negative(self, monkeypatch, comment_instance, comment_info_start, mock_logger,
                                     mock_database):
        mock_database.get_item.side_effect = Exception("Test error")
        comment_instance.comment_id = None

        result = comment_instance.remove_content()

        assert result is None
        mock_database.get_item.assert_called_once_with(Sql.GET_COMMENT_ID.value, (1, "Test Creator"))
        mock_database.remove_item.assert_not_called()
        mock_logger.error.assert_called_once()

    def test_upvote(self):
        pass

    def test_details(self):
        pass
