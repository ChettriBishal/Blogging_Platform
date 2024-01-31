from handlers.comments.get_comment_handler import GetCommentHandler


class GetComments:
    """Has functions to fetch comments for a blog"""
    @staticmethod
    def get_comments_by_blog_id(blog_id):
        all_comments = GetCommentHandler.get_comments_by_blog_id(blog_id)
        return all_comments
