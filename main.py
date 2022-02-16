import sqlite3
import sys

import menu_actions
import pretty_print
import utils

# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def main():
    user_logged_in = False
    user_signed_up = False

    current_menu = "default"
    current_user = None

    # Start the program by greeting the user
    pretty_print.greet_user()

    while True:
        # If user did not logged in/signed up
        if not user_logged_in and not user_signed_up:
            pretty_print.show_default_menu()
        # If user signed up
        if user_signed_up: 
            pretty_print.show_account_created_menu()
            current_menu = "account_created"
        # If user logged in
        if user_logged_in: 
            pretty_print.show_logged_in_menu(current_user)
            current_menu = "logged_in"
                
        # Get user input
        action = utils.get_user_input()

        # Handle actions for default menu
        if current_menu == "default":
            status, user_found = menu_actions.handle_default_menu_actions(action, cursor, connection)

            if status == "user_signed_up":
                user_signed_up = True
                user_logged_in = False
            elif status == "user_logged_in":
                user_logged_in = True
                user_signed_up = False
                current_user = user_found
            
        # Handle actions for account created menu
        elif current_menu == "account_created":
            status, user_found = menu_actions.handle_account_created_menu_actions(action, cursor, connection)

            if status == "user_logged_in":
                user_logged_in = True
                user_signed_up = False
                current_user = user_found

        # Handle actions for logged in menu
        elif current_menu == "logged_in":
            status = menu_actions.handle_logged_in_menu_actions(action, cursor, connection, current_user)

            if status == "user_logged_out":
                user_logged_in = False
                user_signed_up = False
                current_menu = "default"
                pretty_print.greet_user()

if __name__ == "__main__":
    main()