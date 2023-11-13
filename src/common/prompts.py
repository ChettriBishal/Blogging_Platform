from pyfiglet import Figlet

render = Figlet(font='slant')

ENTER_USERNAME = "Enter your username: "
ENTER_PASSWORD = "Enter your password: "
ENTER_EMAIL = "Enter your email address: "

ENTER_BLOG_TITLE = "Enter the title of the blog post: "
ENTER_BLOG_CONTENT = "Enter the post content: "
ENTER_BLOG_TAG = "Enter the tag for the blog: "

ENTER_COMMENT = "Enter the comment: "

HOME_DISPLAY = f"""
{render.renderText("BLOGGING AND QNA")}

1. Sign Up
2. Sign In
3. Exit

Enter your choice: """

BLOGGER_MENU = f"""
{render.renderText("BLOGGER")}
1. View blogs
2. Create a new blog
3. Edit existing blog
4. Remove a blog 
5. Exit
"""

ENTER_NEW_CONTENT = "Enter the new content for the blog: "


