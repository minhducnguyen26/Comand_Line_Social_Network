import pretty_print
import view_user_profile
import view_user_posts
import db_interaction
import utils
import new_feed_actions

def handle_new_feed_menu_actions(action, cursor, connection, current_user):
    done_view_new_feed = False
    # View Self Posts
    if action == 1:
        done_view_new_feed = new_feed_actions.handle_view_self_posts(cursor, connection, current_user)

    # View Friends' Posts
    elif action == 2:
        pretty_print.message("Due to budget constraints, this feature is not available\nPlease try again later.")

    # View Strangers' Posts
    elif action == 3:
        pretty_print.message("Due to budget constraints, this feature is not available\nPlease try again later.")

    # Add Post
    elif action == 4:
        new_feed_actions.handle_add_post(cursor, connection, current_user)

    # Back
    if action == 5:
        pretty_print.message("Return to Main Menu")
        done_view_new_feed = True

    return done_view_new_feed

def handle_options_on_find_people_menu(action, cursor, connection, current_user, people_list):
    done_find_people = False

    if isinstance(action, str):
        # Add Friend
        if action[0] == "3":
            status = db_interaction.handle_add_friend(cursor, connection, current_user, action[1:])

            user_to_find_id = action[1:]
            friend_target = db_interaction.handle_view_user_profile(cursor, connection, user_to_find_id)

            if friend_target:
                if status == "added":
                    pretty_print.message("Congratulations! You are now friends with " + friend_target[1] + ".\nIt will take a little bit to update your changes.")
                elif status == "already friends":
                    pretty_print.message("You are already friends with " + friend_target[1] + ".")
            else:
                pretty_print.message("User not found")

        # Unfriend
        elif action[0] == "4":
            status = db_interaction.handle_remove_friend(cursor, connection, current_user, action[1:])

            user_to_find_id = action[1:]
            friend_target = db_interaction.handle_view_user_profile(cursor, connection, user_to_find_id)

            if friend_target:
                if status == "removed":
                    pretty_print.message("You are no longer friends with " + friend_target[1] + ".\nIt will take a little bit to update your changes.")
                elif status == "not friends":
                    pretty_print.message("You are not friends with " + friend_target[1] + ".")
            else:
                pretty_print.message("User not found")

    else:
        # View User Profile
        done_view_user_profile = False
        if action == 1:
            done_view_user_profile = view_user_profile.main(action, cursor, connection, current_user, people_list)
            pretty_print.message("Returning to Find People Menu")
                
        # View User Posts
        done_view_user_posts = False
        if action == 2:
            done_view_user_posts = view_user_posts.main(action, cursor, connection, current_user, people_list)
            pretty_print.message("Returning to Find People Menu")

        # Go Back
        if action == 5:
            pretty_print.message("Return to Main Menu")
            done_find_people = True

    return done_find_people