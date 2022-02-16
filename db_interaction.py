import sqlite3
from passlib.hash import bcrypt
import getpass

import pretty_print

#! Normal queries
# Add new user to the database (users table)
def handle_create_user(cursor, connection):
    user_signed_up_successfully = False

    while not user_signed_up_successfully:
        pretty_print.message("Create a New Account")

        name = input("Name: ")
        age = input("Age: ")
        email = input("Email: ")

        password = getpass.getpass()
        hashed_password = bcrypt.hash(password)

        # Insert the user into the database
        try:
            cursor.execute("INSERT INTO users (name, age, email, password) VALUES (?, ?, ?, ?)", (name, age, email, hashed_password))
            connection.commit()
            user_signed_up_successfully = True
        except sqlite3.IntegrityError:
            user_signed_up_successfully = False
            connection.rollback()
            
        if user_signed_up_successfully:
            pretty_print.message("Account Created")
        else:
            pretty_print.message("The Email Address Has Been Used. Please Try Again.")

    return user_signed_up_successfully

# Get one user form the database, 
# given their unique email address and password
# Check if the user exists
def handle_verify_user(cursor, connection):
    user_logged_in_successfully = False
    current_user = None

    while not user_logged_in_successfully:
        pretty_print.message("Login")

        email = input("Email: ")
        password = getpass.getpass()

        # Find user person by email
        cursor.execute("SELECT * FROM users WHERE email = ?", [email])
        user_found = cursor.fetchone()

        if user_found:
            # Verify password
            # 3 is the password column
            saved_password = user_found[3]
            verified = bcrypt.verify(password, saved_password)

            if verified:
                user_logged_in_successfully = True
                current_user = user_found
        else:
            user_logged_in_successfully = False

    
        if user_logged_in_successfully:
            pretty_print.message("Login Successful")
        else:
            pretty_print.message("Cannot Find User. Please Try Again.")

    return user_logged_in_successfully, current_user

# Add new post to the database (posts table)
def handle_add_post(cursor, connection, current_user, content):
    cursor.execute("INSERT INTO posts (author_id, content) VALUES (?, ?)", (current_user[0], content))
    connection.commit()

# Get all friends of a user (friendships table)
def handle_find_my_friends(cursor, connection, current_user):
    cursor.execute("SELECT * FROM users WHERE id IN (SELECT from_id FROM friendships WHERE to_id = ?)", [current_user[0]])
    my_friends = cursor.fetchall()
    return my_friends

# Get all users from the database (not current user) and 
# show whether they are friends with the user or not (users table)
def handle_find_people(cursor, connection, current_user):
    pretty_print.message("Find People")

    people_list = []

    # Get all users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # Get all friends
    my_friends = handle_find_my_friends(cursor, connection, current_user)

    for user in users:
        for friend in my_friends:
            if user[0] == friend[0]:
                people_list.append([user[0], user[1], "\u2713"])
                break
        else:
            if user[0] == current_user[0]:
                people_list.append([user[0], user[1], "\u2605"])
            else:
                people_list.append([user[0], user[1], "x"])
    
    return people_list

# Get all information about a user (users table)
def handle_view_user_profile(cursor, connection, user_to_find_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", [user_to_find_id])
    user_found = cursor.fetchone()
    return user_found

# Get all posts from a user (posts table)
def handle_view_user_posts(cursor, connection, user_to_find_id):
    cursor.execute("SELECT * FROM posts WHERE author_id = ?", [user_to_find_id])
    posts = cursor.fetchall()
    return posts

# Get all information about a post's likes (likes table)
def handle_get_posts_likes_infos(cursor, connection, post_id):
    cursor.execute("SELECT * FROM likes WHERE post_id = ?", [post_id])
    likes = cursor.fetchall()
    return likes

# Get all information about a post's dislikes (dislikes table)
def handle_get_posts_dislikes_infos(cursor, connection, post_id):
    cursor.execute("SELECT * FROM dislikes WHERE post_id = ?", [post_id])
    likes = cursor.fetchall()
    return likes

# Get all information about a post's comments (comments table)
def handle_get_post_comments_infos(cursor, connection, post_id):
    cursor.execute("SELECT * FROM comments WHERE post_id = ?", [post_id])
    comments = cursor.fetchall()
    return comments

# Add a like to a post (likes table)
def handle_like_post(cursor, connection, current_user, post_id):
    status = ""
    # Check if the user already liked the post
    cursor.execute("SELECT * FROM likes WHERE user_id = ? AND post_id = ?", (current_user[0], post_id))
    user_already_liked_post = cursor.fetchone()

    # Check if the user already disliked the post
    cursor.execute("SELECT * FROM dislikes WHERE user_id = ? AND post_id = ?", (current_user[0], post_id))
    user_already_disliked_post = cursor.fetchone()

    if user_already_liked_post:
        # Remove the like
        cursor.execute("DELETE FROM likes WHERE user_id = ? AND post_id = ?", (current_user[0], post_id))
        connection.commit()
        status = "unliked"

    elif user_already_disliked_post:
        # Remove the dislike and add a like
        cursor.execute("DELETE FROM dislikes WHERE user_id = ? AND post_id = ?", (current_user[0], post_id))
        cursor.execute("INSERT INTO likes (user_id, post_id) VALUES (?, ?)", (current_user[0], post_id))
        connection.commit()

        status = "liked from disliked"

    else:
        # Add the like
        cursor.execute("INSERT INTO likes (user_id, post_id) VALUES (?, ?)", (current_user[0], post_id))
        connection.commit()
        status = "liked"

    return status

# Add a dislike to a post (dislikes table)
def handle_dislike_post(cursor, connection, current_user, post_id):
    status = ""
    # Check if the user already liked the post
    cursor.execute("SELECT * FROM likes WHERE user_id = ? AND post_id = ?", (current_user[0], post_id))
    user_already_liked_post = cursor.fetchone()

    # Check if the user already disliked the post
    cursor.execute("SELECT * FROM dislikes WHERE user_id = ? AND post_id = ?", (current_user[0], post_id))
    user_already_disliked_post = cursor.fetchone()

    if user_already_disliked_post:
        # Remove the dislike
        cursor.execute("DELETE FROM dislikes WHERE user_id = ? AND post_id = ?", (current_user[0], post_id))
        connection.commit()
        status = "undisliked"

    elif user_already_liked_post:
        # Remove the like and add a dislike
        cursor.execute("DELETE FROM likes WHERE user_id = ? AND post_id = ?", (current_user[0], post_id))
        cursor.execute("INSERT INTO dislikes (user_id, post_id) VALUES (?, ?)", (current_user[0], post_id))
        connection.commit()

        status = "disliked from liked"

    else:
        # Add the dislike
        cursor.execute("INSERT INTO dislikes (user_id, post_id) VALUES (?, ?)", (current_user[0], post_id))
        connection.commit()
        status = "disliked"

    return status

# Add a comment to a post (comments table)
def handle_add_comment_on_post(cursor, connection, post_id, posts_owner, current_user, comment):
    cursor.execute("INSERT INTO comments (author_id, post_id, user_id, content) VALUES (?, ?, ?, ?)", (posts_owner[0], post_id, current_user[0], comment))
    connection.commit()

# Add friendship between two users (friendships table)
def handle_add_friend(cursor, connection, current_user, user_to_add_id):
    status = ""
    # Check if the user is already friends with the user to add
    cursor.execute("SELECT * FROM friendships WHERE to_id = ? AND from_id = ?", (current_user[0], user_to_add_id))
    user_already_friends = cursor.fetchone()

    if user_already_friends:
        status = "already friends"
    
    else:
        # Add the user to the friends table
        cursor.execute("INSERT INTO friendships (to_id, from_id) VALUES (?, ?)", (current_user[0], user_to_add_id))
        connection.commit()
        status = "added"

    return status

# Remove friendship between two users (friendships table)
def handle_remove_friend(cursor, connection, current_user, user_to_remove_id):
    status = ""
    # Check if the user is already friends with the user to add
    cursor.execute("SELECT * FROM friendships WHERE to_id = ? AND from_id = ?", (current_user[0], user_to_remove_id))
    user_already_friends = cursor.fetchone()

    if user_already_friends:
        # Remove the user from the friends table
        cursor.execute("DELETE FROM friendships WHERE to_id = ? AND from_id = ?", (current_user[0], user_to_remove_id))
        connection.commit()
        status = "removed"

    else:
        status = "not friends"

    return status

# Get all information related to the current user's posts (posts, likes, comments, users table):
def handle_view_self_posts(cursor, connection, current_user):
    my_posts = get_all_post_infos(cursor, connection, current_user[0])
    return my_posts

#! "Interesting" queries
# Get all users information and their friend status with the current user (users, friendships table)
def get_all_users_infos_and_friend_status(cursor, connection, current_user):
    cursor.execute('''
        WITH RECURSIVE people_table (person_id, is_friend) AS 
        (
            SELECT 
                my_friend.id, 
                "yes" AS is_friend
            FROM users AS my_friend
            WHERE my_friend.id 
                IN (
                    SELECT from_id 
                    FROM friendships 
                    WHERE to_id = ?
                )

            UNION

            SELECT 
                not_friend.id,
                "no" AS is_friend
            FROM users AS not_friend
            WHERE not_friend.id 
                NOT IN (
                    SELECT from_id 
                    FROM friendships 
                    WHERE to_id = 1
                )
                AND not_friend.id != ?

            UNION

            SELECT
                myself.id,
                "myself" AS is_friend
            FROM users AS myself
            WHERE myself.id = ?

        )
        SELECT users.id, users.name, people_table.is_friend AS is_friend
        FROM people_table
        JOIN users
            ON users.id = people_table.person_id
        ORDER BY person_id;
    ''', [current_user[0], current_user[0], current_user[0]])
    users_infos_and_status = cursor.fetchall()
    return users_infos_and_status

# Get all information related to a post (posts, likes, dislike, comments, table):
def get_all_post_infos(cursor, connection, user_to_find_id):
    cursor.execute("""
        SELECT
        posts.id, posts.created_at, posts.content,
        (SELECT COUNT(*) FROM likes WHERE likes.post_id = posts.id) AS likes,
        (SELECT COUNT(*) FROM dislikes WHERE dislikes.post_id = posts.id) AS dislikes,
        (SELECT COUNT(*) FROM comments WHERE comments.post_id = posts.id) AS comments
        FROM posts
        LEFT JOIN likes 
            ON likes.post_id = posts.id
        LEFT JOIN dislikes 
            ON dislikes.post_id = posts.id
        LEFT JOIN comments 
            ON comments.post_id = posts.id
        WHERE posts.author_id = ?
        GROUP BY posts.id;
    """, [user_to_find_id])

    posts = cursor.fetchall()
    return posts