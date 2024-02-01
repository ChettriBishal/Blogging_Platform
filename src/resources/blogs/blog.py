from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from controllers.blogs.get_blogs import GetBlogs
from controllers.blogs.update_blog import UpdateBlog
from controllers.blogs.remove_blog import RemoveBlog

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

    def put(self, blogId):
        updated_info = request.get_json()
        content = updated_info.get('content')
        title = updated_info.get('title')
        tag = updated_info.get('tag')

        update_blog = UpdateBlog(blog_id=blogId, content=content, title=title, tag=tag)
        if not update_blog.authenticate_user():
            abort(403, detail="Only the writer can edit the blog")

        update_blog.update_content()
        update_blog.update_title()
        update_blog.update_tag()

        return {"message": "Successfully updated the blog"}, 200

    def delete(self, blogId):
        remove_blog = RemoveBlog(blog_id=blogId)
        if not remove_blog.authenticate_user():
            abort(403, detail="Operation not allowed")

        status = remove_blog.remove_blog_by_id()
        if status:
            return {"message": "Successfully removed the blog"}, 200
        abort(500, detail="Could not remove the blog")

