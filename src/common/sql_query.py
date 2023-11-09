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
    SELECT (username,role,email) 
    FROM users 
    """

    GET_USER_BY_USERNAME = """
    SELECT * 
    FROM users
    WHERE username = ?
    """

    GET_PASSWORD = """
    SELECT password 
    FROM users 
    WHERE username = ?
    """
