import db_interaction
import pretty_print
import utils

def handle_view_user_posts(action, cursor, connection, current_user, people_list):
    status = ""
    posts_found = None
    posts_owner = None

    if isinstance(action, str):
        user_to_find_id = action[2:]
        get_posts = db_interaction.get_all_post_infos(cursor, connection, user_to_find_id)
        posts_owner = db_interaction.handle_view_user_profile(cursor, connection, user_to_find_id)

        if len(get_posts) > 0:
            posts_found = get_posts
            status = "user_found_user_posts"
        else:
            status = "user_found_no_posts"

    if action == 2:
        status = "user_returned_to_find_people_menu"

    return status, posts_found, posts_owner

def handle_actions_on_view_user_posts(cursor, connection, posts_found, posts_owner, current_user, people_list):
    done_interact_with_user_posts = False

    pretty_print.message("View User Posts")

    pretty_print.show_user_posts_table_header(posts_owner)

    # Old way using normal queries
    # posts_list = []
    # for post in posts_found:
    #     post_id = post[0]

    #     post_likes_infos = db_interaction.handle_get_posts_likes_infos(cursor, connection, post_id)
    #     handle_get_posts_dislikes_infos = db_interaction.handle_get_posts_dislikes_infos(cursor, connection, post_id)
    #     post_comments_infos = db_interaction.handle_get_post_comments_infos(cursor, connection, post_id)

    #     post_created_at = post[3]
    #     post_content = post[2]

    #     post_likes_count = len(post_likes_infos)
    #     post_dislikes_count = len(handle_get_posts_dislikes_infos)
    #     post_comments_count = len(post_comments_infos)

    #     posts_list.append([post_id, post_created_at, post_content, post_likes_count, post_dislikes_count, post_comments_count])

    # New way using "interesting" queries
    pretty_print.show_user_posts_table(posts_found)

    while not done_interact_with_user_posts:
        pretty_print.show_options_on_user_posts_menu()

        action = utils.get_user_input()
        
        done_interact_with_user_posts = handle_interaction_with_user_posts(action, cursor, connection, posts_found, posts_owner, current_user, people_list)

        if done_interact_with_user_posts:
            pretty_print.message("Return to View User Posts")

    return done_interact_with_user_posts

def handle_interaction_with_user_posts(action, cursor, connection, posts_found, posts_owner, current_user, people_list):
    done_interact_with_user_posts = False

    while not done_interact_with_user_posts:
        if isinstance(action, str):
            post_id = action[2]
            # Like Post
            if action[0] == "1":
                status = db_interaction.handle_like_post(cursor, connection, current_user, post_id)

                if status == "unliked":
                    pretty_print.message("You unliked " + posts_owner[1] + "'s post")
                else:
                    pretty_print.message("You liked " + posts_owner[1] + "'s post")

            # Dislike Post
            if action[0] == "2":
                status = db_interaction.handle_dislike_post(cursor, connection, current_user, post_id)

                if status == "undisliked":
                    pretty_print.message("You undisliked " + posts_owner[1] + "'s post")
                else:
                    pretty_print.message("You disliked " + posts_owner[1] + "'s post")

            # Comment on Post
            if action[0] == "3":
                comment = action[4:].replace('"', "")

                db_interaction.handle_add_comment_on_post(cursor, connection, post_id, posts_owner, current_user, comment)

                pretty_print.message("Comment Added Successfully")

            done_interact_with_user_posts = main(action, cursor, connection, current_user, people_list)
            
        # Go back to View User Posts
        if action == 4:
            done_interact_with_user_posts = main(action, cursor, connection, current_user, people_list)

    return done_interact_with_user_posts

def main(action, cursor, connection, current_user, people_list):
    done_view_user_posts = False
    
    pretty_print.message("View User Posts")
    pretty_print.show_people_table(people_list)

    pretty_print.show_view_actions_on_user_menu()

    action = utils.get_user_input()
    
    status, posts_found, posts_owner = handle_view_user_posts(action, cursor, connection, current_user, people_list)

    while not done_view_user_posts:
        if status == "user_found_user_posts":
            done_view_user_posts = handle_actions_on_view_user_posts(cursor, connection, posts_found, posts_owner, current_user, people_list)
        
        elif status == "user_found_no_posts":
            pretty_print.message(posts_owner[1] + " Has No Posts")
            done_view_user_posts = main(action, cursor, connection, current_user, people_list)
            
        elif status == "user_returned_to_find_people_menu":
            done_view_user_posts = True
    
    return done_view_user_posts