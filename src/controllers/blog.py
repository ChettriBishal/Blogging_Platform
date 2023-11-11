from src.controllers.post import Post
from src.common.sql_query import Sql
from src.models import database


class Blog(Post):
    def __init__(self, blog_info):
        (
            # blog_id will be auto-incremented
            self.title,
            self.content,
            self.creator,
            self.upvotes,
            self.tag_name,
            self.creation_date
        ) = blog_info
        self.blog_info = blog_info

    def add_content(self):
        try:
            database.insert_item(Sql.INSERT_BLOG.value, self.blog_info)
        except Exception as exc:
            print(exc)

    def edit_content(self):
        pass

    def remove_content(self):
        blog_to_remove = database.get_item(Sql.GET_COMMENT_ID.value, (self.title, self.creator))
        try:
            database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (blog_to_remove,))
        except Exception as exc:
            print(exc)

    def upvote(self):
        pass

    def downvote(self):
        pass


if __name__ == "__main__":
    from src.helpers import take_input
    from datetime import datetime

    title, content, tag = take_input.get_blog_post_details()
    rn = datetime.today()
    blog_post_d = (title, content, 'snow123', 0, 'test', rn)
    new_blog = Blog(blog_post_d)
    new_blog.add_content()
