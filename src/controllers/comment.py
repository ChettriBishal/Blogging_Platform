class Comment:
    def __init__(self, comment_info):
        (
            self.comment_id,
            self.user_id,
            self.post_id,
            self.creation_date,
            self.content,
        ) = comment_info

    def add_comment(self):
        pass

    def edit_comment(self, new_content):
        self.content = new_content

    def remove_comment(self):
        pass
        # invoke a destructor here ?
