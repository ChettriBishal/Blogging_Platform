from models.database import Database
from config.sql_query_mysql import Sql
from loggers.general_logger import GeneralLogger
from config import filepaths


class RemoveBlogHandler:
    @staticmethod
    def remove_blog(blog_id):
        """
        This function allows the user to remove his blogs
        """
        title = take_input.get_title()
        blog_details = Database.get_item(Sql.GET_BLOG_RECORD.value, (title, active_user.username))

        if blog_details is None:
            print(prompts.BLOG_NOT_FOUND_BLOG_USER.format(title, active_user.username))
            return Flag.DOES_NOT_EXIST.value

        # create blogs object
        current_blog = Blog(blog_details[1:])
        current_blog.set_blog_id(blog_details[0])

        blog_removed = current_blog.remove_content()

        if blog_removed:
            print(prompts.BLOG_REMOVED.format(title))
            GeneralLogger.info(prompts.BLOG_REMOVED.format(title), filepaths.BLOG_LOG_FILE)

        else:
            print(prompts.COULD_NOT_REMOVE_BLOG)
