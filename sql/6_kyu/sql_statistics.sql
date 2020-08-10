/*
SQL Statistics: MIN, MEDIAN, MAX
5 kyu

For this challenge you need to create a simple SELECT statement. Your task is to calculate the MIN, MEDIAN and MAX scores of the students from the results table.

Resultant table:
min
median
max
*/

SELECT
	MIN(score) as min,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY score) as median,
	MAX(score) as max
FROM result;