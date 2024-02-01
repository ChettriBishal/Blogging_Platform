from handlers.comments.update_comment_handler import UpdateCommentHandler
from utils.users.get_current_user import GetCurrentUser
from handlers.comments.comment_info_handler import CommentInfoHandler


# you can update content of the comment
class UpdateComment:
    def __init__(self, **kwargs):
        self.blog_id = kwargs.get('blog_id')
        self.comment_id = kwargs.get('comment_id')
        self.content = kwargs.get('content')

    def authenticate_user(self):
        """Authenticate that the current user in session has commented on the blog"""
        current_userid = GetCurrentUser.get_user_id()
        creator_id = CommentInfoHandler.get_creator_id_for_comment(self.blog_id, self.comment_id)
        if current_userid != creator_id:
            return False
        return True

    def update_content(self):
        """Update the actual blog content"""
        if self.content:
            update_status = UpdateCommentHandler.update_comment(self.comment_id, self.content)
            return update_status

