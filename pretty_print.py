def greet_user():
    print("")
    print("=========================================================")
    print("      Welcome to the Command Line Social Network \nwhere you can connect to people and share your thoughts.")
    print("=========================================================")

def message(message):
    print("")
    print("=========================================================")
    print(message)
    print("=========================================================")

def show_default_menu():
    print("""
    Menu:
    1. Sign Up
    2. Login
    3. Exit
    """)

def show_account_created_menu():
    print("""
    Menu:
    1. Verify Account
    2. Exit
    """)

def show_logged_in_menu(current_user):
    show_user_photo_and_name(current_user)
    print("""
    Menu:
    1. New Feed
    2. Add Post
    3. Find People
    4. Logout
    """)

def show_options_on_people_menu():
    print("""
    Menu:
    1. View User Profile
    2. View User Posts
    3. Add Friend (Type: 3 + space + user ID)
    4. Unfriend (Type: 4 + space + user ID)
    5. Back
    """)

def show_view_actions_on_user_menu():
    print("""
    Menu:
    1. Type: 1 + space + user ID
    2. Back
    """)

def show_people_table(people_list):
    print("")
    print("{: <5} {: <20} {: <20}".format("ID", "Name", "Friend"))
    print("{: <5} {: <20} {: <20}".format("____", "___________________", "________"))
    for row in people_list:
        print("{: <5} {: <20} {: <20}".format(*row))

def show_user_info_table(user):
    name = user[1]
    email = user[2]
    age = user[4]
    print("")
    print("{: <14} {: <18} {: <20}".format("Name", "Email", "Age"))
    print("{: <14} {: <18} {: <20}".format("____________", "________________", "___"))
    print("{: <14} {: <18} {: <20}".format(name, email, age))

def show_user_photo_and_name(user):
    print("")
    print("\U0001F464" + " " + user[1])

def show_user_posts_table_header(posts_owner):
    show_user_photo_and_name(posts_owner)
    print("")
    print("{: <5} {: <25} {: <40} {: <10} {: <10} {: <15}".format("ID", "Created At", "Content", "Likes", "Dislikes", "Comments"))
    print("{: <5} {: <25} {: <40} {: <10} {: <10} {: <15}".format("____", "_____________________", "_____________________________________", "_______", "__________", "__________"))

def show_user_posts_table(posts_list):
    for row in posts_list:
        print("{: <5} {: <25} {: <40} {: <10} {: <10} {: <15}".format(*row))

def go_back_menu(): 
    print("""
    Menu:
    1. Back
    """)

def show_options_on_user_posts_menu():
    print("""
    Menu:
    1. Like Post (Type: 1 + space + post ID)
    2. Dislike Post (Type: 2 + space + post ID)
    3. Comment on Post (Type: 3 + space + post ID + space + "your_comment")
    4. Back
    """)

def show_new_feed_option_menu():
    print("""
    Menu:
    1. View Self Posts
    2. View Friends' Posts
    3. View Strangers' Posts
    4. Add Post 
    5. Back
    """)

def user_post_template(post_author, post, comment_list):
    print("")
    show_user_photo_and_name(post_author)
    print("")
    print("ID: " + str(post[0]))
    print("Content: ")
    print("     " + post[2])
    print("Created At: " + post[1])
    print("Likes: " + str(post[3]))
    print("Dislikes: " + str(post[4]))

    if len(comment_list) > 0:
        print("Comments: ")
        for comment in comment_list:
            if comment != comment_list[-1]:
                print("    |")
                print("    |__\U0001F464" + " " + comment[0])
                print("    |  Content: " + comment[1])
                print("    |  Created At: " + str(comment[2]))
            else:
                print("    |")
                print("    |__\U0001F464" + " " + comment[0])
                print("       Content: " + comment[1])
                print("       Created At: " + str(comment[2]))
    else:
        print("No comments yet.")
    
def show_view_self_posts_menu():
    print("""
    Menu:
    1. Like Post (Type: 1 + space + post ID)
    2. Dislike Post (Type: 2 + space + post ID)
    3. Comment on Post (Type: 3 + space + post ID + space + "your_comment")
    4. Back
    """)