from enum import Enum


class SQL(Enum):
    CREATE_USER_TABLE = """
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT,password TEXT, role TEXT,
    email TEXT, registration_date DATE
    )
    """

    CREATE_POST_TABLE = """
    CREATE TABLE IF NOT EXISTS posts (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    creator_id INTEGER,
    upvotes INTEGER,
    post_type TEXT,
    tag_name TEXT,
    FOREIGN KEY (creator_id) REFERENCES users(user_id)
    )
    """
