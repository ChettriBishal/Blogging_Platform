import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

BLOGGING_DB = os.path.join(project_root, 'storage', 'user.db')

USER_LOG_FILE = os.path.join(project_root, 'storage', 'user.log')

BLOG_LOG_FILE = os.path.join(project_root, 'storage', 'blog.log')

COMMENT_LOG_FILE = os.path.join(project_root, 'storage', 'comment.log')

DB_LOG_FILE = os.path.join(project_root, 'storage', 'db.log')

SYSTEM_LOG_FILE = os.path.join(project_root, 'storage', 'system.log')

APP_LOG_FILE = os.path.join(project_root, 'storage', 'app.log')
