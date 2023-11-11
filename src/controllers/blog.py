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
            self.tag_name
        ) = blog_info
        self.post_info = blog_info

    def add_content(self):
        try:
            database.insert_item(Sql.INSERT_POST.value, self.post_info)
        except Exception as exc:
            print(exc)

    def remove_content(self):
        pass

