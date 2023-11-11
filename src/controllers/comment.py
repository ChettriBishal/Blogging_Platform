from src.controllers.post import Post
from src.common.sql_query import Sql
from src.models import database


class Comment(Post):
    def __init__(self, comment_info):
        (
            # comment_id will be auto incremented
            self.blog_id,
            self.content,
            self.creator,
            self.upvotes,
            self.creation_date,
        ) = comment_info
        self.comment_id = None
        self.comment_info = comment_info

    def add_content(self):
        try:
            self.comment_id = database.insert_item(Sql.INSERT_COMMENT.value, self.comment_info)
        except Exception as exc:
            print(exc)

    def edit_content(self, new_content):
        try:
            comment_id = database.get_item(Sql.GET_COMMENT_ID.value, (self.blog_id, self.creator,))[0]
            database.query_with_params(Sql.EDIT_COMMENT.value, (new_content, comment_id,))
            return True
        except Exception as exc:
            print(exc)

    def remove_content(self):
        comment_to_remove = database.get_item(Sql.GET_COMMENT_ID.value, (self.blog_id, self.creator))
        try:
            database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (comment_to_remove,))
        except Exception as exc:
            print(exc)

    def upvote(self, user_id):
        upvote_record = database.get_item(Sql.CHECK_COMMENT_UPVOTE.value, (user_id, self.comment_id,))
        if upvote_record is None:
            self.upvotes += 1
            database.insert_item(Sql.ADD_COMMENT_UPVOTE.value, (user_id, self.comment_id,))
            database.query_with_params(Sql.UPDATE_COMMENT_UPVOTE.value, (self.upvotes, self.comment_id,))
            return True
        else:
            return False

    def downvote(self):
        pass

    def show_details(self):
        username = database.get_item(Sql.GET_USERNAME_BY_USERID.value, (self.creator,))[0]
        return(f"""
        Author: {username}
        Comment: {self.content}
        Written on: {self.creation_date}
        """)


if __name__ == "__main__":
    from src.helpers import take_input
    from datetime import datetime

    # content = take_input.get_comment()
    # rn = datetime.today()
    # comment_d = (1, content, 'snow123', 0, rn)
    comment_d = (1, "xyz", 'snow123', 0, 'no worries')
    new_c = Comment(comment_d)
    # new_blog.add_content()
    # if new_blog.edit_content("changed this comment as well"):
    #     print("Edited comment successfully")
    # else:
    #     print("Could not edit comment")
    new_c.comment_id = 1
    new_c.upvote(3)
