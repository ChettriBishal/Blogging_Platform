from models.comment import Comment
from datetime import datetime
from config.filepaths import COMMENT_LOG_FILE
from config import prompts
from loggers.general_logger import GeneralLogger


class AddComment:
    """
    This allows users to add comments to blogs
    """

    def add_comment(self, blog_id, content, creator_id):

        current_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        comment_info = (blog_id, content, creator_id, 0, current_time)

        new_comment = Comment(comment_info)
        status = new_comment.add_content()

        if status:
            return True
        else:
            return False
