import requests
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint('Comments', __name__, description='Operations related to comments')


@blp.route('/blogs/<string:blogId>/comments')
class BlogComments(MethodView):
    def get(self, blogId):
        return {"message": f"Comments for blog id {blogId}"}

    def post(self, blogId):
        return {"message": f"Added a new comment to {blogId}"}


@blp.route('/blogs/<string:blogId>/comments/<string:commentId>')
class GetSpecificCommentForBlog(MethodView):
    def get(self, blogId, commentId):
        return {"message": f"Comment {commentId} for blog {blogId}"}

