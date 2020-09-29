-- Easy SQL: Counting and Grouping
-- 7 kyu

/*
Given a demographics table in the following format:

** demographics table schema **

id
name
birthday
race
you need to return a table that shows a count of each race represented, ordered by the count in descending order as:

** output table schema **

race
count
*/

SELECT race, COUNT(id)
FROM demographics
GROUP BY 1
ORDER BY 2 DESC;