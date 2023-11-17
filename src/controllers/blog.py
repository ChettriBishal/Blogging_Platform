from src.controllers.post import Post
from src.common.sql_query import Sql
from src.utils import database
from src.controllers.comment import Comment
from src.loggers.general_logger import GeneralLogger
from src.common import filepaths
from src.common import prompts


class Blog(Post):
    def __init__(self, blog_info):
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

    def add_content(self):
        try:
            self.blog_id = database.insert_item(Sql.INSERT_BLOG.value, self.blog_info)

        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)

    def set_blog_id(self, blog_id):
        self.blog_id = blog_id

    def edit_content(self, new_content):
        try:
            if self.blog_id is None:
                self.blog_id = database.get_item(Sql.GET_BLOG_ID.value, (self.title, self.creator,))[0]

            database.query_with_params(Sql.EDIT_BLOG.value, (new_content, self.blog_id,))

            return True

        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)

    def remove_content(self):
        try:
            if self.blog_id is None:
                self.blog_id = database.get_item(Sql.GET_BLOG_ID.value, (self.title, self.creator))

            self.remove_comments()
            database.remove_item(Sql.REMOVE_BLOG_BY_ID.value, (self.blog_id,))

            return True

        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)

    def upvote(self, user_id):
        upvote_record = database.get_item(Sql.CHECK_BLOG_UPVOTE.value, (user_id, self.blog_id,))

        if upvote_record is None:
            self.upvotes += 1
            database.query_with_params(Sql.ADD_BLOG_UPVOTE.value, (user_id, self.blog_id,))
            database.query_with_params(Sql.UPDATE_BLOG_UPVOTE.value, (self.upvotes, self.blog_id,))

            return True

        else:
            return False

    def details(self):
        blog_info = (self.title, self.creator, self.tag_name, self.creation_date, self.content, self.upvotes)

        return prompts.BLOG_DETAILS.format(*blog_info)

    def get_comments(self):
        all_comments = database.get_items(Sql.GET_COMMENT_BY_BLOG_ID.value, (self.blog_id,))
        blog_comments = [Comment(record[1:]) for record in all_comments]

        return blog_comments

    def remove_comments(self):
        all_comments = database.get_items(Sql.GET_COMMENTS_BY_BLOG_ID.value, (self.blog_id,))

        for comment_id in all_comments:
            comment_to_remove = comment_id[0]
            database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (comment_to_remove,))

            GeneralLogger.info(prompts.REMOVED_COMMENT_WITH_ID.format(comment_id[0]), filepaths.COMMENT_LOG_FILE)
