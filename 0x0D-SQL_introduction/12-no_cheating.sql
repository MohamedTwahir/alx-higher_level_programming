-- script that updates the score of Bob to 10 in the table second_table
-- no using id only name field
-- database name will be passed as an argument
UPDATE second_table
SET `score` = 10
WHERE `name` = 'Bob';
