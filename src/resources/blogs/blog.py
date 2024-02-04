from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from controllers.blogs.get_blogs import GetBlogs
from controllers.blogs.update_blog import UpdateBlog
from controllers.blogs.remove_blog import RemoveBlog
from config.constants import authorization_bearer
from config.message import Message

blp = Blueprint('Blog', __name__, description='Operations on blogs')


@blp.route('/blogs')
class GetAllBlogs(MethodView):
    def get(self):
        blogs = GetBlogs.get_all_blogs()
        return blogs


@blp.route('/blogs/<int:blogId>')
class GetSpecificBlog(MethodView):
    def get(self, blogId):
        blog = GetBlogs.get_single_blog(blogId)
        return blog

    @blp.doc(parameters=authorization_bearer)
    def put(self, blogId):
        updated_info = request.get_json()
        content = updated_info.get('content')
        title = updated_info.get('title')
        tag = updated_info.get('tag')

        update_blog = UpdateBlog(blog_id=blogId, content=content, title=title, tag=tag)
        if not update_blog.authenticate_user():
            abort(403, detail=Message.OPERATION_NOT_ALLOWED)

        update_blog.update_content()
        update_blog.update_title()
        update_blog.update_tag()

        return {"message": Message.SUCCESSFUL_UPDATE}, 200

    @blp.doc(parameters=authorization_bearer)
    def delete(self, blogId):
        remove_blog = RemoveBlog(blog_id=blogId)
        if not remove_blog.authenticate_user():
            abort(403, detail=Message.OPERATION_NOT_ALLOWED)

        status = remove_blog.remove_blog_by_id()
        if status:
            return {"message": Message.SUCCESSFUL_REMOVAL}, 200
        abort(500, detail=Message.FAILURE_IN_REMOVAL)

