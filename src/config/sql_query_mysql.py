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

    CREATE_BLOG_UPVOTES_TABLE = """
    CREATE TABLE IF NOT EXISTS blog_upvotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    blog_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (blog_id) REFERENCES blogs(blog_id)  
    )
    """

    ADD_BLOG_UPVOTE = """
    INSERT INTO blog_upvotes (user_id, blog_id) 
    VALUES (%s,%s)
    """

    UPDATE_BLOG_UPVOTE = """
    UPDATE blogs 
    SET upvotes = %s 
    WHERE blog_id = %s
    """

    CHECK_BLOG_UPVOTE = """
    SELECT * FROM blog_upvotes 
    WHERE user_id = %s AND blog_id = %s
    """

    ADD_COMMENT_UPVOTE = """
    INSERT INTO comment_upvotes (user_id, comment_id) 
    VALUES (%s,%s)
    """

    UPDATE_COMMENT_UPVOTE = """
    UPDATE comments 
    SET upvotes = %s 
    WHERE comment_id = %s
    """

    CHECK_COMMENT_UPVOTE = """
    SELECT * FROM comment_upvotes 
    WHERE user_id = %s AND comment_id = %s
    """

    GET_COMMENTS_BY_BLOG_ID = """
    SELECT comment_id 
    FROM comments 
    WHERE blog_id = %s
    """

    CREATE_COMMENT_UPVOTES_TABLE = """
    CREATE TABLE IF NOT EXISTS comment_upvotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    comment_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (comment_id) REFERENCES comments(comment_id)  
    )
    """

    INSERT_USER = """
    INSERT INTO users (username, password, role, email, registration_date)
    VALUES (%s,%s,%s,%s,%s)
    """

    REMOVE_USER_BY_USERNAME = """
    DELETE FROM users 
    WHERE username = %s
    """

    UPDATE_PASSWORD = """
    UPDATE users 
    SET password = %s
    WHERE username = %s
    """

    GET_ALL_USERS = """
    SELECT *
    FROM users 
    """

    GET_USER_BY_USERNAME = """
    SELECT * 
    FROM users
    WHERE username = %s;
    """

    GET_USER_ID_BY_USERNAME = """
    SELECT user_id
    FROM users 
    WHERE username = %s;
    """

    GET_USER_BY_EMAIL = """
    SELECT * 
    FROM users
    WHERE email = %s;
    """

    GET_USERID_BY_USERNAME = """
    SELECT user_id
    FROM users
    WHERE username = %s
    """

    GET_USERNAME_BY_USERID = """
    SELECT username
    FROM users
    WHERE user_id = %s
    """

    GET_PASSWORD = """
    SELECT password 
    FROM users 
    WHERE username = %s
    """

    INSERT_BLOG = """
    INSERT INTO blogs(title,content,creator_id,upvotes,tag_name,creation_date)
    VALUES(%s,%s,%s,%s,%s,%s)
    """

    EDIT_BLOG = """
    UPDATE blogs 
    SET content = %s 
    WHERE blog_id = %s 
    """

    GET_BLOG_ID = """
    SELECT blog_id 
    FROM blogs 
    WHERE title = %s AND creator_id = %s
    """

    GET_BLOGS_BY_USERNAME = """
    SELECT * 
    FROM blogs 
    WHERE creator_id = %s
    """

    GET_BLOGS_BY_TAG_NAME = """
    SELECT * 
    FROM blogs
    WHERE tag_name = %s
    """

    GET_BLOG_RECORD = """
    SELECT * 
    FROM blogs 
    WHERE title = %s AND creator_id = %s
    """

    GET_BLOG_RECORD_BY_TITLE = """
    SELECT * 
    FROM blogs 
    WHERE title = %s
    """

    GET_COMMENT_ID = """
    SELECT comment_id 
    FROM comments 
    WHERE blog_id = %s AND creator_id = %s
    """

    GET_COMMENT_BY_BLOG_ID = """
    SELECT * 
    FROM comments 
    WHERE blog_id = %s
    """

    INSERT_COMMENT = """
    INSERT INTO comments(blog_id,content,creator_id,upvotes,creation_date)
    VALUES(%s,%s,%s,%s,%s)
    """

    EDIT_COMMENT = """
    UPDATE comments 
    SET content = %s 
    WHERE comment_id = %s 
    """

    REMOVE_BLOG_BY_ID = """
    DELETE FROM blogs 
    WHERE blog_id = %s
    """

    REMOVE_BLOG_BY_TITLE = """
    DELETE FROM blogs 
    WHERE title = %s
    """

    REMOVE_COMMENT_BY_ID = """
    DELETE FROM comments 
    WHERE comment_id = %s
    """

    GET_ALL_BLOGS = """
    SELECT * FROM blogs
    """

