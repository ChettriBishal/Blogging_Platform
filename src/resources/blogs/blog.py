import requests
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from controllers.blog import Blog
from controllers.blogs.create_blog import CreateBlog
from schemas.blog_schema import BlogSchema

blp = Blueprint('Blog', __name__, description='Operations on blogs')


@blp.route('/blogs')
class GetAllBlogs(MethodView):
    def get(self):
        return {"message": "Will update this tomorrow gotta wait"}


@blp.route('/blogs/<string:blogId>')
class GetSpecificBlog(MethodView):
    def get(self, blogId):
        return {"message": f"Showing blog {blogId}"}


# posting a blog
# @blp.route('/users/<int:userId>/blogs')
# class BlogUser(MethodView):

