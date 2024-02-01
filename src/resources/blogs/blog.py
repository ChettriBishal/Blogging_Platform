from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from controllers.blogs.get_blogs import GetBlogs
from controllers.blogs.update_blog import UpdateBlog

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
        # if content and not update_blog.update_content():
        #     pass
        # if title and update_blog.update_title():
        #     pass
        # if tag and update_blog.update_tag():
        #     pass

# put operation on a blog, just check if the creator id is same as the current user in session
