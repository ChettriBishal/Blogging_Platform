class Post:
    """
    Attributes and methods associated with blogs and comments alike
    """

    def __init__(self, post_info):
        (
            self.post_id,
            self.title,
            self.content,
            self.creator,
            self.upvotes,
            self.post_type,
            self.tag_name
        ) = post_info
        # db must contain these fields in this order only

    @classmethod
    def new_post(cls, post_info):
        post_id = None  # generate post id here
        post_info = (post_id,) + post_info
        return cls(post_info)
