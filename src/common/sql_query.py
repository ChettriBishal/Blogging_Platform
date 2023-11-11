from enum import Enum


class Sql(Enum):
    CREATE_USER_TABLE = """
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT,password TEXT, role TEXT,
    email TEXT, registration_date DATE
    )
    """

    DELETE_POSTS_TABLE = """
    drop table posts;
    """

    CREATE_BLOG_TABLE = """
    CREATE TABLE IF NOT EXISTS blogs (
    blog_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    creator_id INTEGER,
    upvotes INTEGER,
    tag_name TEXT,
    FOREIGN KEY (creator_id) REFERENCES users(user_id)
    )
    """

    CREATE_COMMENTS_TABLE = """
    CREATE TABLE IF NOT EXISTS comments (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    blog_id INTEGER,
    content TEXT,
    creator_id INTEGER,
    upvotes INTEGER,
    FOREIGN KEY (creator_id) REFERENCES users(user_id),
    FOREIGN KEY (blog_id) REFERENCES blogs(blog_id)
    )
    """

    INSERT_USER = """
    INSERT INTO users (username, password, role, email, registration_date)
    VALUES (?,?,?,?,?)
    """

    REMOVE_USER = """
    DELETE FROM users 
    WHERE username = ?
    """

    UPDATE_PASSWORD = """
    UPDATE users 
    SET password = ?
    WHERE username = ?
    """

    GET_ALL_USERS = """
    SELECT username,role,email
    FROM users 
    """

    GET_USER_BY_USERNAME = """
    SELECT * 
    FROM users
    WHERE username = ?
    """

    GET_USERID_BY_USERNAME = """
    SELECT user_id
    FROM users
    WHERE username = ?
    """

    GET_PASSWORD = """
    SELECT password 
    FROM users 
    WHERE username = ?
    """

# fix this
    INSERT_POST = """
    INSERT INTO posts (title,content,creator_id,upvotes, post_type, tag_name)
    VALUES (?,?,?,?,?,?)
    """
