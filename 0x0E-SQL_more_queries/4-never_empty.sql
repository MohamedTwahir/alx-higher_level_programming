-- script that creates the table id_not_null on MySQL server
-- description:
-- id INT with default value 1
-- name VARCHAR(256)
-- database name will be passed on as argument
-- if table already exists script should not fail
CREATE TABLE
    IF NOT EXISTS id_not_null(id INT DEFAULT 1,name VARCHAR(256));
