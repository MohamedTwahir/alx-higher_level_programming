-- a script that lists all records with a score >= 10 in second_table of database
-- results should display both the score and name
-- record should be in correct order
-- database name will be passed as argument
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
