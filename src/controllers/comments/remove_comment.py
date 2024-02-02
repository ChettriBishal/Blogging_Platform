from utils.users.get_current_user import GetCurrentUser
from handlers.comments.comment_info_handler import CommentInfoHandler
from handlers.comments.remove_comment_handler import RemoveCommentHandler


# you can update content of the comment
class RemoveComment:
    def __init__(self, **kwargs):
        self.blog_id = kwargs.get('blog_id')
        self.comment_id = kwargs.get('comment_id')

    def authenticate_user(self):
        """Authenticate that the current user in session has commented on the blog"""
        current_userid = GetCurrentUser.get_user_id()
        creator_id = CommentInfoHandler.get_creator_id_for_comment(self.blog_id, self.comment_id)
        if current_userid != creator_id:
            return False
        return True

    def remove_comment(self):
        """Remove comment by its ID"""
        comment_removed = RemoveCommentHandler.remove_comment_by_id(self.comment_id)
        return comment_removed

