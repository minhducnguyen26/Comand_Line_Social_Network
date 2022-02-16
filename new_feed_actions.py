import pretty_print
import utils
import db_interaction

def handle_view_self_posts(cursor, connection, current_user):
    pretty_print.message("Your Posts")

    done_view_self_posts = False
    while not done_view_self_posts:
        my_posts = db_interaction.handle_view_self_posts(cursor, connection, current_user)

        if len(my_posts) == 0:
            pretty_print.message("No posts found. Consider adding one.")

        post_author = current_user
        for post in my_posts:

            comment_list = []
            comments = db_interaction.handle_get_post_comments_infos(cursor, connection, post[0])
            for comment in comments:
                comment_author_id = db_interaction.handle_view_user_profile(cursor, connection, comment[3])
                comment_content = comment[4]
                comment_created_at = comment[5]

                comment_list.append([comment_author_id[1], comment_content, comment_created_at])

            pretty_print.user_post_template(post_author, post, comment_list)

        pretty_print.show_view_self_posts_menu()

        action = utils.get_user_input()

        if isinstance(action, str):
            post_id = action[2]
            # Like Post
            if action[0] == "1":
                status = db_interaction.handle_like_post(cursor, connection, current_user, post_id)

                if status == "unliked":
                    pretty_print.message("Unlike Post Successful")
                else:
                    pretty_print.message("Like Post Successful")

            # Dislike Post
            if action[0] == "2":
                status = db_interaction.handle_dislike_post(cursor, connection, current_user, post_id)

                if status == "undisliked":
                    pretty_print.message("Undislike Post Successful")
                else:
                    pretty_print.message("Dislike Post Successful")

            # Comment on Post
            if action[0] == "3":
                comment = action[4:].replace('"', "")

                db_interaction.handle_add_comment_on_post(cursor, connection, post_id, current_user, current_user, comment)

                pretty_print.message("Comment Added Successfully")

        else:
            if action == 4:
                pretty_print.message("Return to New Feed")
                done_view_self_posts = True

def handle_add_post(cursor, connection, current_user):
    pretty_print.message("Create a New Post")

    print("What's on your mind, " + current_user[1] + "?")
    content = input("> ")

    db_interaction.handle_add_post(cursor, connection, current_user, content)

    pretty_print.message("Post Added Successfully")