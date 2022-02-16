-- Create new users
INSERT INTO users (name, email, password, age) VALUES ('Minh Nguyen', 'minh@gmail.com', '$2b$12$SB3Qbu06bVn7jdWwvPE4xOEQA6HP6hlobDLYLYqWfZ8lNqae1L17i', 21);
INSERT INTO users (name, email, password, age) VALUES ('Tony Stark', 'tony@gmail.com', '$2b$12$6BCassdSBS5ONe8FlZr3muifRTdRpe94gr05fSGwjxzySdbz.8R5S', 45);
INSERT INTO users (name, email, password, age) VALUES ('Steve Rogers', 'steve@gmail.com', '$2b$12$iFAr.fmFmhaugejlXDEgO.nDIxCwEcyQ9LKv3j18oLESFbkGda04e', 95);
INSERT INTO users (name, email, password, age) VALUES ('Bruce Banner', 'bruce@gmail.com', '$2b$12$uftCryIeYVbFcakL1L9iLujj00QTY5u2Cn7bxFwiH4O/Rf3RToCKm', 40);
INSERT INTO users (name, email, password, age) VALUES ('Thor', 'thor@gmail.com', '$2b$12$MT4uMKmH/8z8lQ0q4JyKEe5yQnsiY2fpBowr7Cljwx31JdW7yb8Fm', 3035);
INSERT INTO users (name, email, password, age) VALUES ('Natasha Romanoff', 'nat@gmail.com', '$2b$12$pejNBQ/G7ymbYLjAMmpWdet4JEx96/AZA/xxWMeGrfvrHb7df9xci', 29);
INSERT INTO users (name, email, password, age) VALUES ('Clint Barton', 'clint@gmail.com', '$2b$12$HlPtQByRLCkf6H1/8T1Bee7LnisH1OO4QDxHfSwh1ELTkbx/V9tma', 32);
INSERT INTO users (name, email, password, age) VALUES ('Peter Parker', 'peter@gmail.com', '$2b$12$riJvzhwAs6fHE/PHVd28E.2dg6gn/nti3CBjSM55o9FreOSaLAbNe', 16);
INSERT INTO users (name, email, password, age) VALUES ('Peter Quill', 'star@gmail.com', '$2b$12$5MuhqbfwY4lHLsNmYMSHROOcAk.WS73.MBe7CyijzzRnMXcEF6JXe', 52);
INSERT INTO users (name, email, password, age) VALUES ('Wanda Maximoff', 'wanda@gmail.com', '$2b$12$okqfyZqnrECCHqbmVbfEsOkvazQWj14s0IktmwSi64uzi86B3r7MG', 27);

-- Create friendships
INSERT INTO friendships (to_id, from_id) VALUES (1, 2);
INSERT INTO friendships (to_id, from_id) VALUES (1, 3);
INSERT INTO friendships (to_id, from_id) VALUES (1, 8);
INSERT INTO friendships (to_id, from_id) VALUES (2, 3);
INSERT INTO friendships (to_id, from_id) VALUES (2, 4);
INSERT INTO friendships (to_id, from_id) VALUES (2, 5);
INSERT INTO friendships (to_id, from_id) VALUES (2, 6);
INSERT INTO friendships (to_id, from_id) VALUES (3, 2);
INSERT INTO friendships (to_id, from_id) VALUES (4, 6);
INSERT INTO friendships (to_id, from_id) VALUES (6, 7);
INSERT INTO friendships (to_id, from_id) VALUES (7, 6);
INSERT INTO friendships (to_id, from_id) VALUES (8, 10);

-- Create posts
INSERT INTO posts (author_id, content) VALUES (1, 'Hello, I am Minh Nguyen');
INSERT INTO posts (author_id, content) VALUES (2, 'I love Avengers');
INSERT INTO posts (author_id, content) VALUES (2, 'Give me back my shields, @Steve');

-- Create comments
INSERT INTO comments (author_id, post_id, user_id, content) VALUES (1, 1, 2, 'Welcome to the community, kid.');
INSERT INTO comments (author_id, post_id, user_id, content) VALUES (2, 2, 4, 'So do I, @Tony');
INSERT INTO comments (author_id, post_id, user_id, content) VALUES (2, 3, 3, 'Nah bro, @Tony');
INSERT INTO comments (author_id, post_id, user_id, content) VALUES (2, 3, 5, 'Give it back, @Steve, you got my hammer ;)');

-- Create likes
INSERT INTO likes (user_id, post_id) VALUES (2, 1);
INSERT INTO likes (user_id, post_id) VALUES (9, 2);
INSERT INTO likes (user_id, post_id) VALUES (1, 2);
INSERT INTO likes (user_id, post_id) VALUES (6, 3);

-- Create dislikes
INSERT INTO dislikes (user_id, post_id) VALUES (3, 3);