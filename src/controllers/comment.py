class Comment:
    def __init__(self, comment_info):
        (
            self.comment_id,
            self.user_id,
            self.post_id,
            self.creation_date,
            self.content,
        ) = comment_info
