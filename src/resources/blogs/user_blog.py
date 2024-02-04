from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from controllers.blogs.create_blog import CreateBlog
from controllers.blogs.get_blogs import GetBlogs
from config.constants import authorization_bearer

blp = Blueprint("User_blog", __name__, description="User blogs operations")


@blp.route('/users/<int:userId>/blogs')
class BlogsFromId(MethodView):
    def get(self, userId):
        access_blog = GetBlogs(user_id=userId)
        blogs = access_blog.get_blogs_by_username()
        return blogs

    @jwt_required()
    # @blp.arguments(BlogPostSchema)
    @blp.doc(parameters=authorization_bearer)
    def post(self, userId):
        blog_info = request.get_json()
        blog_creation = CreateBlog(blog_info.values())
        blog_creation.user_id = userId
        blog_creation_response = blog_creation.create_new_blog()
        return blog_creation_response



