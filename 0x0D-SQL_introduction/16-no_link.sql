-- a script that lists all records of the second_table of databsae
-- dont list rows without name
-- results should display score and name in the order
-- records should be listed by asceding score
-- database name will be passed as an argument
SELECT `score` `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
