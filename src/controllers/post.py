from abc import ABC, abstractmethod


class Post(ABC):
    """
    Attributes and methods associated with blogs and comments alike
    """

    @abstractmethod
    def add_content(self):
        pass

    @abstractmethod
    def remove_content(self):
        pass

    def get_post_by_user_id(self):
        pass

    def upvote(self):
        pass

    def downvote(self):
        pass


