-- script that lists all cities of California found in database hbtn_0d_usa
-- states table contains only one record name = California id can be different
-- result must be sorted in ascending order by cities.id
-- not allowed to use JOIN keyword
-- database name will be passed as an argument
SELECT `id`, `name`
  FROM `cities
WHERE `state_id` IN
      (SELECT `id`
	FROM `states`
	WHERE `name` = "California")
ORDER BY `id`;
