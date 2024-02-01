from flask import request
from flask.views import MethodView

from flask_jwt_extended import jwt_required

from flask_smorest import Blueprint, abort
from controllers.blogs.create_blog import CreateBlog
from controllers.blogs.get_blogs import GetBlogs

blp = Blueprint("User_blog", __name__, description="User blogs operations")


@blp.route('/users/<int:userId>/blogs')
class BlogsFromId(MethodView):
    def get(self, userId):
        access_blog = GetBlogs(user_id=userId)
        blogs = access_blog.get_blogs_by_username()
        return blogs

    @jwt_required()
    # @blp.arguments(BlogPostSchema)
    def post(self, userId):
        blog_info = request.get_json()
        blog_creation = CreateBlog(blog_info.values())
        blog_creation.user_id = userId
        blog_added = blog_creation.create_new_blog()
        if blog_added:
            return {"message": f"{userId} successfully added a blog!"}, 201
        abort(500, message="Could not post blogs")



