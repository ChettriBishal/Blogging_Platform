from datetime import date


class BlogResponse:
    def __init__(self, blog_info):
        (
            self.blog_id,
            self.title,
            self.content,
            self.creator_id,
            self.upvotes,
            self.tag_name,
            self.creation_date
        ) = blog_info

    def to_dict(self):
        return {
            "blog_id": self.blog_id,
            "title": self.title,
            "content": self.content,
            "creator_id": self.creator_id,
            "upvotes": self.upvotes,
            "tag_name": self.tag_name,
            "creation_date": self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
            if isinstance(self.creation_date, date) else str(self.creation_date)
        }
