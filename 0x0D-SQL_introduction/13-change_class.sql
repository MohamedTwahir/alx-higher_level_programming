-- script that removes all records with score <= 5 in second_table
-- database name will be passed as argument
DELETE FROM second_table
WHERE `score` <= 5;
