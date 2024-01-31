from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from controllers.comments.add_comment import AddComment
from controllers.comments.get_comments import GetComments

blp = Blueprint('Comments', __name__, description='Operations related to comments')


@blp.route('/blogs/<int:blogId>/comments')
class BlogComments(MethodView):
    def get(self, blogId):
        comments = GetComments.get_comments_by_blog_id(blogId)
        if comments:
            return comments, 200
        abort(404, detail="No comments present for this blogs")

    @jwt_required()
    def post(self, blogId):
        comment_info = request.get_json()
        content = comment_info.get('content')
        comment_object = AddComment(content=content, blog_id=blogId)
        comment_added = comment_object.add_comment()
        if comment_added:
            return {"message": f"Added a new comments to {blogId}"}, 201
        abort(500, detail="Could not comments to the blogs")


@blp.route('/blogs/<int:blogId>/comments/<int:commentId>')
class GetSpecificCommentForBlog(MethodView):
    def get(self, blogId, commentId):
        return {"message": f"Comment {commentId} for blogs {blogId}"}
