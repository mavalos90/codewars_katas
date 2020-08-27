/*
SQL Basics: Simple PIVOTING data WITHOUT CROSSTAB
6 kyu

This kata is inspired by SQL Basics: Simple PIVOTING data by matt c.

You need to build a pivot table WITHOUT using CROSSTAB function. Having two tables products and details you need to select a pivot table of products with counts of details occurrences (possible details values are ['good', 'ok', 'bad'].
Results should be ordered by product's name.

Model schema for the kata is:

products
	id
	name
	
details
	id
	product_id
	detail

your query should return table with next columns

name
good
ok
bad
*/

SELECT p.name AS name,
       COUNT(CASE WHEN d.detail = 'good' THEN 1 END) AS good,
       COUNT(CASE WHEN d.detail = 'ok' THEN 1 END) AS ok,
       COUNT(CASE WHEN d.detail = 'bad' THEN 1 END) AS bad
FROM 
	products p
INNER JOIN 
	details d
ON p.id = d.product_id
GROUP BY p.name
ORDER BY p.name