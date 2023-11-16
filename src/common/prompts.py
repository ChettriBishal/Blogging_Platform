from pyfiglet import Figlet

render = Figlet(font='slant')

ENTER_USERNAME_TO_REMOVE = "Enter the username to remove: "
ENTER_USERNAME = "Enter your username: "
ENTER_USERNAME_FOR_BLOGS = "Enter username to get blogs: "
ENTER_PASSWORD = "Enter your password: "
ENTER_NEW_PASSWORD = "Enter your new password: "
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
2. View blogs by a user
3. View a single blog
4. Create a new blog
5. Edit existing blog
6. Remove a blog 
7. Upvote a blog
8. Comment on a blog
9. Change password
10. Exit

Enter your choice: """

ENTER_NEW_CONTENT = "Enter the new content for the blog: "

COMMENTS = "--------------Comments--------------"

ADMIN_SPECIFIC = f"""
{render.renderText("ADMIN")}
1. View blogs
2. View blogs by a user
3. View a single blog
4. Create a new blog
5. Edit existing blog
6. Remove a blog 
7. Upvote a blog
8. Comment on a blog
9. List all users
10. Remove user by username
11. Change Password
12. Exit

Enter your choice: """

CHOOSE_ANOTHER_TITLE = "A blog by this title already exists. Please choose another one!"

SYSTEM_START = "The app has started"

SYSTEM_EXIT = "The app has finished running"

ENTER_VALID_CHOICE = "Please enter a valid choice!"

