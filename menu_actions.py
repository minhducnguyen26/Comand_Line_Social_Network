import sys

import db_interaction
import pretty_print
import utils
import logged_in_menu

# Default Menu - Main
def handle_default_menu_actions(action, cursor, connection):
    user_logged_in = False
    user_signed_up = False
    user_found = None

    # Sign Up
    if action == 1:
        user_signed_up = db_interaction.handle_create_user(cursor, connection)
    
    # Login
    elif action == 2:
        user_logged_in, user_found = db_interaction.handle_verify_user(cursor, connection)

    # Exit
    elif action == 3:
        print("")
        sys.exit(0)

    if user_signed_up:
        return "user_signed_up", user_found
    elif user_logged_in:
        return "user_logged_in", user_found

# Account Created Menu - Main
def handle_account_created_menu_actions(action, cursor, connection):  
    user_logged_in = False

    # Verify Account
    if action == 1:
        user_logged_in, user_found = db_interaction.handle_verify_user(cursor, connection)
    
    # Exit
    elif action == 2:
        print("")
        sys.exit(0)

    if user_logged_in:
        return "user_logged_in", user_found

# Logged In Menu - Main
def handle_logged_in_menu_actions(action, cursor, connection, current_user):
    # New Feed
    if action == 1:
        pretty_print.message("Today's New Feed")

        done_view_new_feed = False
        while not done_view_new_feed:
            pretty_print.show_new_feed_option_menu()

            action = utils.get_user_input()

            done_view_new_feed = logged_in_menu.handle_new_feed_menu_actions(action, cursor, connection, current_user)

    # Add Post
    if action == 2:
        pretty_print.message("Create a New Post")

        print("What's on your mind, " + current_user[1] + "?")
        content = input("> ")

        db_interaction.handle_add_post(cursor, connection, current_user, content)

        pretty_print.message("Post Added Successfully")

    # Find People
    if action == 3:
        # Old way using normal queries
        # people_list = db_interaction.handle_find_people(cursor, connection, current_user)

        # New way using "interesting queries"
        users_infos_and_status = db_interaction.get_all_users_infos_and_friend_status(cursor, connection, current_user)
        people_list = []

        for people in users_infos_and_status:
            # Convert people tuple to list
            user = list(people)

            # If is friend
            if user[2] == "yes":
                user[2] = "\u2713"

            # If is not friend
            elif user[2] == "no":
                user[2] = "x"

            # If is the user itself
            elif user[2] == "myself":
                user[2] = "\u2605"

            people_list.append(user)

        done_find_people = False
        while not done_find_people:
            pretty_print.show_people_table(people_list)

            pretty_print.show_options_on_people_menu()

            action = utils.get_user_input()

            done_find_people = logged_in_menu.handle_options_on_find_people_menu(action, cursor, connection, current_user, people_list)

    # Logout
    if action == 4:
        pretty_print.message("Logout Successful")
        return "user_logged_out"
