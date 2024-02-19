from flask import request
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from flask_smorest import Blueprint
from controllers.blogs.get_blogs import GetBlogs
from controllers.blogs.update_blog import UpdateBlog
from controllers.blogs.remove_blog import RemoveBlog
from config.constants import authorization_bearer

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

    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    def put(self, blogId):
        updated_info = request.get_json()
        content = updated_info.get('content')
        title = updated_info.get('title')
        tag = updated_info.get('tag')

        update_blog = UpdateBlog(blog_id=blogId, content=content, title=title, tag=tag)
        update_blog_status = update_blog.update_the_blog()
        return update_blog_status

    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    def delete(self, blogId):
        remove_blog = RemoveBlog(blog_id=blogId)
        status = remove_blog.remove_blog_by_id()
        return status

