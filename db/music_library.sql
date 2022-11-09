DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY, 
    full_name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    artist_id INT REFERENCES artists(id) ON DELETE CASCADE
);

INSERT INTO artists (full_name) 
VALUES ('Chance The Rapper');

INSERT INTO artists (full_name) 
VALUES ('Lady Gaga');

INSERT INTO artists (full_name) 
VALUES ('Keith Richards');
