-- script that creates a table called first_table in the current database in my MySQL server
-- database name will be passed as an argument of sql command
-- if table exists script should not fail
-- not allowed to use SELECT or SHOW
CREATE TABLE  IF NOT EXISTS `first_table`(`id` INT, `name` VARCHAR(256));
