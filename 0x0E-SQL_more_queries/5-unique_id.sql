-- script that creates th table unique_id on my MySQL server
-- description:
-- id INT with the default value 1 and must be unique
-- name VARCHAR(256)
-- database name will be passed on as argument
-- if table already exists, script should not fail
CREATE TABLE
    IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
