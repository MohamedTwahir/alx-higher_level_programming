-- script that creates the database hbtn_0d_usa and the table states in that database
-- description
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
-- script shouldn't fail if database and table exists
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE
    IF NOT EXISTS `hbtn_0d_usa`.`states`(
	`id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        `name` VARCHAR(256) NOT NULL
);	
