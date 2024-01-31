from models.database import Database
from config.sql_query_mysql import Sql
from loggers.general_logger import GeneralLogger
from config import filepaths


class UpdateBlogHandler:
    @staticmethod
    def update_blog_title(blog_id, new_title):
        try:
            Database.query_with_params(Sql.EDIT_BLOG_TITLE.value, (new_title, blog_id,))
            return True
        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)
            return False

    @staticmethod
    def update_blog_content(blog_id, new_content):
        try:
            Database.query_with_params(Sql.EDIT_BLOG_CONTENT.value, (new_content, blog_id,))
            return True
        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)
            return False

    @staticmethod
    def update_blog_tag(blog_id, new_tag):
        try:
            Database.query_with_params(Sql.EDIT_BLOG_TITLE.value, (new_tag, blog_id,))
            return True
        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)
            return False
