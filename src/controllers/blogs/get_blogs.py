from config import prompts
from handlers.blogs.get_blogs_handler import GetBlogsHandler
from handlers.user.user_info_handler import UserInfoHandler
from config.flags import Flag
from models.blog_response import BlogResponse


class GetBlogs:
    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.username = kwargs.get('username')

        if 'user_id' not in kwargs and 'username' in kwargs:
            UserInfoHandler.get_user_id_by_username(kwargs['username'])
        elif 'username' not in kwargs and 'user_id' in kwargs:
            self.username = UserInfoHandler.get_username_by_userid(kwargs['user_id'])

    # def blog_info_to_json(self, blog_info):

    @staticmethod
    def get_all_blogs():
        """
        To get all the blogs posted so far
        """
        blogs = GetBlogsHandler.blog_collection()
        return blogs

    @staticmethod
    def get_single_blog():
        """Get a single blog by id"""

    # UPDATE you have to use userid to fetch the blogs now
    @staticmethod
    def get_blogs_by_userid(userid):
        """Get blogs by a specific user using his user id (using his for consistency) """
        # firstly get the username using userid

    def get_blogs_by_username(self):
        """
        To view blogs by a particular user using his username
        """

        print(f"First line of the get blogs by username function")
        if self.username is None:
            return Flag.INVALID_OPERATION.value

        print("After the if condition")
        blogs = GetBlogsHandler.blogs_by_username(self.username)

        if len(blogs) < 1:
            blogs = None

        if blogs is None:
            # return 404
            print(prompts.NO_BLOG_BY_USER.format(self.username))
            return

        blog_responses = []
        for blog_response in blogs:
            blog_responses.append(BlogResponse(blog_response).to_dict())
        return blog_responses

        # blogs = [Blog(blog[1:]) for blog in blogs]
        # for blog in blogs:
        #     print(blog.details())
