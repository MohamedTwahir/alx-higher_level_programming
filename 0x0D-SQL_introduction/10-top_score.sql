-- script that lists all records of the table second_table in my server
-- results should display both the score and name in order
-- database name will be passed as an argument
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
