"""This module contains various operations performed on a blog"""

from typing import Union, Tuple, List
from controllers.post import Post
from config.sql_query import Sql
from models.database import Database
from controllers.comment import Comment
from loggers.general_logger import GeneralLogger
from config import filepaths
from config import prompts


class Blog(Post):
    """
    Class containing various methods possible on a blog
    """
    def __init__(self, blog_info: Tuple) -> None:
        (
            # blog_id will be auto-incremented
            self.title,
            self.content,
            self.creator,
            self.upvotes,
            self.tag_name,
            self.creation_date
        ) = blog_info
        self.blog_id = None
        self.blog_info = blog_info

    def add_content(self) -> Union[bool, None]:
        """
        Method to add a new content
        """
        try:
            self.blog_id = Database.insert_item(Sql.INSERT_BLOG.value, self.blog_info)
            if self.blog_id:
                return True
            # return False

        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)

    def set_blog_id(self, blog_id: str) -> None:
        """
        Method to set the blog id to a blog object
        """
        self.blog_id = blog_id

    def edit_content(self, new_content: str) -> Union[bool, None]:
        """
        Method to edit the blog content associated to a blog object
        """
        try:
            if self.blog_id is None:
                self.blog_id = Database.get_item(Sql.GET_BLOG_ID.value, (self.title, self.creator,))[0]

            Database.query_with_params(Sql.EDIT_BLOG.value, (new_content, self.blog_id,))

            return True

        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)

    def remove_content(self) -> Union[bool, None]:
        """
        Method to remove the content associated with a blog object
        """
        try:
            if self.blog_id is None:
                self.blog_id = Database.get_item(Sql.GET_BLOG_ID.value, (self.title, self.creator))

            self.remove_comments()
            Database.remove_item(Sql.REMOVE_BLOG_BY_ID.value, (self.blog_id,))

            return True

        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)

    def upvote(self, user_id: str) -> bool:
        """
        Method which allows user to upvote a blog
        """
        upvote_record = Database.get_item(Sql.CHECK_BLOG_UPVOTE.value, (user_id, self.blog_id,))

        if upvote_record is None:
            self.upvotes += 1
            Database.query_with_params(Sql.ADD_BLOG_UPVOTE.value, (user_id, self.blog_id,))
            Database.query_with_params(Sql.UPDATE_BLOG_UPVOTE.value, (self.upvotes, self.blog_id,))

            return True

        else:
            return False

    def details(self) -> str:
        """
        Method to return the details of the blog
        """
        blog_info = (self.title, self.creator, self.tag_name, self.creation_date, self.content, self.upvotes)

        return prompts.BLOG_DETAILS.format(*blog_info)

    def get_comments(self) -> Union[List[Comment], None]:
        """
        Method to get the comments present in the blog
        """
        all_comments = Database.get_items(Sql.GET_COMMENT_BY_BLOG_ID.value, (self.blog_id,))
        if all_comments:
            blog_comments = [Comment(record[1:]) for record in all_comments]
            return blog_comments
        else:
            return None

    def remove_comments(self) -> None:
        """
        Method to remove all the comments present in the blog
        """
        all_comments = Database.get_items(Sql.GET_COMMENTS_BY_BLOG_ID.value, (self.blog_id,))

        for comment_id in all_comments:
            comment_to_remove = comment_id[0]
            Database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (comment_to_remove,))

            GeneralLogger.info(prompts.REMOVED_COMMENT_WITH_ID.format(comment_id[0]), filepaths.COMMENT_LOG_FILE)

    def remove_content_by_title(self) -> bool:
        """
        Method to remove the blog content by the title name
        """
        if self.blog_id is None:
            self.blog_id = Database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (self.title,))

        self.remove_comments()
        Database.remove_item(Sql.REMOVE_BLOG_BY_ID.value, (self.blog_id,))

        return True
