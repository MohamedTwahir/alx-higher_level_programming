-- script that creates the table force_name on my MySQL server
-- description:
-- id INT
-- name VARCHAR(256) can't be null
-- database name will be passed on as an argument
-- if table already exists your script should not fail
CREATE TABLE
    IF NOT EXISTS force_name(id INT, name VARCHAR(256) NOT NULL);
