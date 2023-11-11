from enum import Enum


class Sql(Enum):
    CREATE_USER_TABLE = """
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT,password TEXT, role TEXT,
    email TEXT, registration_date DATE
    )
    """

    CREATE_BLOG_TABLE = """
    CREATE TABLE IF NOT EXISTS blogs (
    blog_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    creator_id INTEGER,
    upvotes INTEGER,
    tag_name TEXT,
    creation_date DATE,
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
    creation_date DATE,
    FOREIGN KEY (creator_id) REFERENCES users(user_id),
    FOREIGN KEY (blog_id) REFERENCES blogs(blog_id)
    )
    """

    INSERT_USER = """
    INSERT INTO users (username, password, role, email, registration_date)
    VALUES (?,?,?,?,?)
    """

    REMOVE_USER_BY_USERNAME = """
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

    INSERT_BLOG = """
    INSERT INTO blogs(title,content,creator_id,upvotes,tag_name,creation_date)
    VALUES(?,?,?,?,?,?)
    """

    GET_BLOG_ID = """
    SELECT blog_id 
    FROM blogs 
    WHERE title = ? AND creator_id = ?
    """

    GET_COMMENT_ID = """
    SELECT comment_id 
    FROM comments 
    WHERE blog_id = ? AND creator_id = ?
    """

    INSERT_COMMENT = """
    INSERT INTO comments(blog_id,content,creator_id,upvotes,creation_date)
    VALUES(?,?,?,?,?)
    """

    REMOVE_BLOG_BY_ID = """
    DELETE FROM blogs 
    WHERE blog_id = ?
    """

    REMOVE_COMMENT_BY_ID = """
    DELETE FROM comments 
    WHERE comment_id = ?
    """
