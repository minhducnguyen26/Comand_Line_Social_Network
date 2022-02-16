def get_user_input():
    user_input = input("What would you like to do? ")

    # If the user input requires information
    if len(user_input) == 1:
        action = int(user_input)

    # If the user input is a single number
    else:
        action = user_input
        
    return action