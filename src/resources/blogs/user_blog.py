import requests
from flask import request
from flask.views import MethodView
from config.flags import Flag
from flask import jsonify
from controllers.user import User

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt

from flask_smorest import Blueprint, abort
from controllers.blogs.create_blog import CreateBlog
from schemas.blog_schema import BlogSchema, BlogPostSchema

blp = Blueprint("User_blog", __name__, description="User blog operations")


@blp.route('/users/<string:userId>/blogs')
class BlogsFromId(MethodView):
    def get(self, userId):
        return {"message": f"{userId} Watch Imitation Game"}

    @jwt_required()
    # @blp.arguments(BlogPostSchema)
    def post(self, userId):
        blog_info = request.get_json()
        blog_creation = CreateBlog(blog_info.values())
        blog_added = blog_creation.create_new_blog()
        if blog_added:
            return {"message": f"{userId} successfully added a blog!"}
        abort(500, message="Could not post blog")


@blp.route('/users/<string:userId>/blogs')
class GetUserBlogById(MethodView):
    def get(self, userId):
        blogId = requests.args.get('blogId')
        return {"message": f"Blog with id {blogId} by userId {userId}"}
