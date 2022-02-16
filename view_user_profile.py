import db_interaction
import pretty_print
import utils

def handle_view_user_profile(action, cursor, connection, current_user):
    status = ""
    user_found = None

    if isinstance(action, str):
        user_to_find_id = action[2:]
        get_user = db_interaction.handle_view_user_profile(cursor, connection, user_to_find_id)

        if get_user:
            user_found = get_user
            status = "user_found_user_profile"

    if action == 2:
        status = "user_returned_to_find_people_menu"

    return status, user_found

def handle_actions_on_view_user_profile(user_found):
    pretty_print.message("Profile for " + user_found[1])
    
    pretty_print.show_user_info_table(user_found)

    pretty_print.go_back_menu()

    action = utils.get_user_input()

    if action == 1:
        return True

def main(action, cursor, connection, current_user, people_list):
    done_view_user_profile = False

    pretty_print.message("View User Profile")
    pretty_print.show_people_table(people_list)

    pretty_print.show_view_actions_on_user_menu()

    action = utils.get_user_input()
    
    status, user_found = handle_view_user_profile(action, cursor, connection, current_user)

    if status == "user_found_user_profile":
        done_view_user_profile = handle_actions_on_view_user_profile(user_found)
        
    elif status == "user_returned_to_find_people_menu":
        done_view_user_profile = True
    
    return done_view_user_profile