class Post:
    """
    Attributes and methods associated with blogs and comments alike
    """

    def __init__(self, post_info):
        (
            #post_id will be auto-incremented
            self.title,
            self.content,
            self.creator,
            self.upvotes,
            self.post_type,
            self.tag_name
        ) = post_info
        # db must contain these fields in this order only

    def add_post(self):  # add using this class object
        pass

    def remove_post(self):
        pass

    def get_post_by_user_id(self):
        pass

    def upvote(self):
        pass

    def downvote(self):
        pass
