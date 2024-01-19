import requests
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint('Blog', __name__, description='Operations on blogs')


@blp.route('/blogs')
class GetAllBlogs(MethodView):
    def get(self):
        return {"message": "Will update this tomorrow gotta wait"}


@blp.route('/blogs/<string:blogId>')
class GetSpecificBlog(MethodView):
    def get(self, blogId):
        return {"message": f"Showing blog {blogId}"}
