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
{render.renderText("BLOGGING & QNA")}

1. Sign Up
2. Sign In
3. Exit

Enter your choice: """

BLOGGER_MENU = f"""
{render.renderText("BLOGGER")}
1. View blogs
2. View a single blog
3. Create a new blog
4. Edit existing blog
5. Remove a blog 
6. Upvote a blog
7. Comment on a blog
8. Exit

Enter your choice: """

ENTER_NEW_CONTENT = "Enter the new content for the blog: "

COMMENTS = "--------------Comments--------------"

ADMIN_SPECIFIC = f"""
{render.renderText("ADMIN")}
1. View blogs
2. View a single blog
3. Create a new blog
4. Edit existing blog
5. Remove a blog 
6. Upvote a blog
7. Comment on a blog
8. List all users
9. Remove user by username
10. Exit

Enter your choice: """


