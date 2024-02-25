from datetime import datetime
from utils.exceptions import DbException
from utils.users.get_current_user import GetCurrentUser
from handlers.user.user_info_handler import UserInfoHandler
from handlers.comments.add_comment_handler import AddCommentHandler


class AddComment:
    """
    This allows users to add comments to blogs
    """

    def __init__(self, **kwargs):
        self.blog_id = kwargs.get('blog_id')
        self.content = kwargs.get('content')
        self.creator_id = None
        self.creation_date = None
        self.comment_info = None

    def structure_comment_info(self):
        """Structure comment data for insertion into database"""

        current_user = GetCurrentUser.get_user_name()
        self.creator_id = UserInfoHandler.get_user_id_by_username(current_user)[0]
        self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.comment_info = (self.blog_id, self.content, self.creator_id, 0, self.creation_date)

    def add_comment(self):
        """To add a new comments to a blogs"""
        try:
            self.structure_comment_info()
            comment_id = AddCommentHandler.add_new_comment(self.comment_info)

            if comment_id:
                return comment_id
            else:
                return False
        except DbException as exc:
            return exc.dump()
