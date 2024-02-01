from handlers.comments.get_comment_handler import GetCommentHandler


class GetComments:
    """Has functions to fetch comments for a blogs"""

    @staticmethod
    def get_comments_by_blog_id(blog_id):
        all_comments = GetCommentHandler.get_comments_by_blog_id(blog_id)
        return all_comments

    @staticmethod
    def get_specific_comment(blog_id, comment_id):
        comment = GetCommentHandler.get_comment_by_comment_id(blog_id, comment_id)
        return comment
