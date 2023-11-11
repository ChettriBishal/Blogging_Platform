from abc import ABC, abstractmethod


class Post(ABC):
    """
    Attributes and methods associated with blogs and comments alike
    """

    @abstractmethod
    def add_content(self):
        pass

    @abstractmethod
    def edit_content(self, new_content):
        pass

    @abstractmethod
    def remove_content(self):
        pass

    @abstractmethod
    def upvote(self):
        pass

    @abstractmethod
    def downvote(self):
        pass

    @abstractmethod
    def show_details(self):
        pass
