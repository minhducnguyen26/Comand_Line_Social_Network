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
            WHERE to_id = 1
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
        AND not_friend.id != 1

    UNION

    SELECT
        myself.id,
        "myself" AS is_friend
    FROM users AS myself
    WHERE myself.id = 1

)
SELECT 
    users.id, users.name, people_table.is_friend AS is_friend
FROM people_table
JOIN users
    ON users.id = people_table.person_id
ORDER BY person_id;

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
WHERE posts.author_id = 1
GROUP BY posts.id;