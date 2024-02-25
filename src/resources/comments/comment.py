from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from controllers.comments.add_comment import AddComment
from controllers.comments.get_comments import GetComments
from controllers.comments.update_comment import UpdateComment
from controllers.comments.remove_comment import RemoveComment
from config.constants import authorization_bearer
from config.message import Message

blp = Blueprint('Comments', __name__, description='Operations related to comments')


@blp.route('/blogs/<int:blogId>/comments')
class BlogComments(MethodView):
    def get(self, blogId):
        comments = GetComments.get_comments_by_blog_id(blogId)
        if comments:
            return comments, 200
        abort(404, detail=Message.NO_COMMENT_FOUND)

    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    def post(self, blogId):
        comment_info = request.get_json()
        content = comment_info.get('content')
        comment_object = AddComment(content=content, blog_id=blogId)
        comment_added = comment_object.add_comment()
        if comment_added:
            return {"commentId": comment_added, "message": Message.SUCCESSFUL_POST}, 201
        abort(500, detail=Message.COULD_NOT_COMMENT)


@blp.route('/blogs/<int:blogId>/comments/<int:commentId>')
class GetSpecificCommentForBlog(MethodView):
    def get(self, blogId, commentId):
        comment = GetComments.get_specific_comment(blogId, commentId)
        if comment:
            return comment, 200
        abort(404, detail=Message.RESOURCE_NOT_FOUND)

    @blp.doc(parameters=authorization_bearer)
    def put(self, blogId, commentId):
        comment_info = request.get_json()
        update_comment = UpdateComment(blog_id=blogId, comment_id=commentId, content=comment_info.get('content'))
        if not update_comment.authenticate_user():
            abort(403, detail=Message.OPERATION_NOT_ALLOWED)

        update_comment.update_content()
        return {"message": Message.SUCCESSFUL_UPDATE}, 200

    @blp.doc(parameters=authorization_bearer)
    def delete(self, blogId, commentId):
        remove_comment = RemoveComment(blog_id=blogId, comment_id=commentId)
        if not remove_comment.authenticate_user():
            abort(403, detail=Message.OPERATION_NOT_ALLOWED)

        remove_comment.remove_comment()
        return {"message": Message.SUCCESSFUL_REMOVAL}, 200
