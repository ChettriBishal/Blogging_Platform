from flask.views import MethodView
from flask_smorest import Blueprint

from controllers.blogs.get_blogs import GetBlogs

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

