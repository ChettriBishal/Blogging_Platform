from datetime import date


class CommentResponse:
    def __init__(self, comment_info):
        (
            self.comment_id,
            self.blog_id,
            self.content,
            self.creator_id,
            self.upvotes,
            self.creation_date
        ) = comment_info

    def to_dict(self):
        return {
            "comment_id": self.comment_id,
            "blog_id": self.blog_id,
            "content": self.content,
            "creator_id": self.creator_id,
            "upvotes": self.upvotes,
            "creation_date": self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
            if isinstance(self.creation_date, date) else str(self.creation_date)
        }
