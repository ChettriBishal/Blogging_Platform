from src.controllers.post import Post
from src.common.sql_query import Sql
from src.models import database
from src.controllers.comment import Comment


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
        self.blog_id = None
        self.blog_info = blog_info

    def add_content(self):
        try:
            self.blog_id = database.insert_item(Sql.INSERT_BLOG.value, self.blog_info)
        except Exception as exc:
            print(exc)

    def set_blog_id(self, blog_id):
        self.blog_id = blog_id

    def edit_content(self, new_content):
        # firstly get the blog_id
        try:
            if self.blog_id is None:
                self.blog_id = database.get_item(Sql.GET_BLOG_ID.value, (self.title, self.creator,))[0]
            database.query_with_params(Sql.EDIT_BLOG.value, (new_content, self.blog_id,))
            return True
        except Exception as exc:
            print(exc)

    def remove_content(self):
        try:
            if self.blog_id is None:
                self.blog_id = database.get_item(Sql.GET_BLOG_ID.value, (self.title, self.creator))

            self.remove_comments()
            database.remove_item(Sql.REMOVE_BLOG_BY_ID.value, (self.blog_id,))
            return True
        except Exception as exc:
            print(exc)

    def upvote(self, user_id):
        upvote_record = database.get_item(Sql.CHECK_BLOG_UPVOTE.value, (user_id, self.blog_id,))
        if upvote_record is None:
            self.upvotes += 1
            database.query_with_params(Sql.ADD_BLOG_UPVOTE.value, (user_id, self.blog_id,))
            database.query_with_params(Sql.UPDATE_BLOG_UPVOTE.value, (self.upvotes, self.blog_id,))
            return True
        else:
            return False

    def details(self):
        return (f"""
        Title: {self.title}
        Author: {self.creator}
        Created on: {self.creation_date}
        Content: {self.content}
        Upvotes: {self.upvotes}
        """)

    def get_comments(self):
        all_comments = database.get_items(Sql.GET_COMMENT_BY_BLOG_ID.value, (self.blog_id,))

        blog_comments = [Comment(record[1:]) for record in all_comments]
        # for comment in all_comments:

        return blog_comments

    def remove_comments(self):
        # get all those comments which have the same blog_id
        all_comments = database.get_items(Sql.GET_COMMENTS_BY_BLOG_ID.value, (self.blog_id,))

        for comment_id in all_comments:
            comment_to_remove = comment_id[0]
            database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (comment_to_remove,))


if __name__ == "__main__":
    from src.helpers import take_input
    from datetime import datetime

    # title, content, tag = take_input.get_blog_post_details()
    # rn = datetime.today()
    # blog_post_d = ('YUI', 'just testing', 'snow123', 0, 'test', '2023-11-11 18:16:08.792008')
    blog_post_d = ('Study faster', 'just testing', 'test123', 0, 'test', '2023-11-11 18:16:08.792008')
    # blog_post_d = (title, content, 'snow123', 0, tag, rn)
    new_blog = Blog(blog_post_d)
    # new_blog.show_details()
    # new_blog.add_content()
    # if new_blog.edit_content("Change to this"):
    #     print("Edited successfully!")
    # else:
    #     print("Failed to edit!")
    new_blog.blog_id = 6
    # # new_blog.upvote(2)
    # comments = new_blog.get_comments()
    #
    # for comment in comments:
    #     print(comment.details())
    # print(*new_blog.get_comments())
    new_blog.remove_comments()
