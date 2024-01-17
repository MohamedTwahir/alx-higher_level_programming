-- script that creates a table in server and ads multiple rows
-- records where given in the question to be inserted in the table
CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(1, 'John', 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(2, 'Alex', 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(3, 'Bob', 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(4, 'George', 8);
