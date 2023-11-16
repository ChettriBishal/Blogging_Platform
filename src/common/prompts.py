from pyfiglet import Figlet

render = Figlet(font='slant')

ENTER_USERNAME_TO_REMOVE = "Enter the username to remove: "

ENTER_USERNAME = "Enter your username: "

ENTER_USERNAME_FOR_BLOGS = "Enter username to get blogs: "

ENTER_PASSWORD = "Enter your password: "

ENTER_STRONG_PASSWORD = """
While choosing a password have the following: 
1. At least one uppercase letter
2. At least one lowercase letter
3. At least one digit
4. Minimum length of 8 characters

Try again...
"""

ENTER_NEW_PASSWORD = "Enter your new password: "

ENTER_EMAIL = "Enter your email address: "

ENTER_VALID_EMAIL = "Enter a valid email address "

ENTER_BLOG_TITLE = "Enter the title of the blog post: "

ENTER_BLOG_CONTENT = "Enter the post content: "

ENTER_BLOG_TAG = "Enter the tag for the blog: "

ENTER_COMMENT = "Enter the comment: "

USER_SIGNED_UP = "User with username `{}` has signed up successfully!"

USER_LOGGED_IN = "User with username `{}` has signed in successfully"

USER_DOES_NOT_EXIST = "This user does not exist."

PLEASE_TRY_AGAIN = "Please try again..."

DISPLAY_USER_HEADER = "\nUsername\t\tRole\t\tEmail"

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

SIGNUP = "---------------SIGN UP---------------"

SIGNIN = "---------------SIGN IN---------------"

USERS_HEADER = "--------------USERS--------------"


USER_INFO = "{}\t|\t{}\t|\t{}"

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

ENTER_VALID_USERNAME = """
Consider the following while choosing a username: 
1. It can contain letters (uppercase, lowercase)
2. It can contain numbers
3. It can contain underscore

Try again...
"""

USERNAME_ALREADY_EXISTS = "This username `{}` already exists"

BLOG_NOT_FOUND_BLOG_USER = "Can't find `blog {}` written by `{}`!"

SUCCESSFUL_PASSWORD_CHANGE = "Password changed successfully!"

USER_CHANGED_PASSWORD = "`{}` has changed their password!"

COMMENT_ADDED = "Comment has been added successfully!"

USER_REMOVED = "User removed successfully!"

USER_WITH_USERNAME_REMOVED = "User with username `{}` has been removed"

BLOG_ADDED = "\n{} has been added!"

COMMENT_NOT_ADDED = "Comment could not be added!"

WRONG_PASSWORD = "Wrong Password! Please try again..."

BLOG_EDITED = "`{}` was edited successfully!"

COULD_NOT_EDIT_BLOG = "Could not edit the blog `{}`"

REMOVED_COMMENT_WITH_ID = "Removed comment with id `{}`"

BLOG_REMOVED = "Blog with title `{}` has been removed!"

COULD_NOT_REMOVE_BLOG = "Could not remove the blog!"

UPVOTED_BLOG = "Blog with title `{}` has been upvoted!"

COULD_NOT_UPVOTE_BLOG = "Could not upvote blog `{}` again!"

USER_COMMENTED = "`{}` commented on the blog `{}`"

BLOG_DETAILS = """
Title: {}

Author: {}

Created on: {}

Content: {}

Upvotes: {}

"""

