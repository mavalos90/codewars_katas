/*
SQL Basics: Simple table totalling
6 kyu

For this challenge you need to create a simple query to display each unique clan with their total points and ranked by their total points.
people table schema
	name
	points
	clan
You should then return a table that resembles below
	rank
	clan
	total_points
	total_people
The query must rank each clan by their total_points, you must return each unqiue clan and if there is no clan name (i.e. it's an empty string) you must replace it with [no clan specified], you must sum the total_points for each clan and the total_people within that clan.
*/



SELECT
    RANK() OVER(ORDER BY SUM(points) DESC) as rank,
    CASE WHEN clan = '' THEN '[no clan specified]'
    ELSE clan END AS clan,
    SUM(points) AS total_points,
    COUNT(name) AS total_people
FROM people
GROUP BY clan