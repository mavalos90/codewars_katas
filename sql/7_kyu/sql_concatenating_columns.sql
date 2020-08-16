/*
SQL: Concatenating Columns
7 kyu

Given the table below:
** names table schema **
	id
	prefix
	first
	last
	suffix

Your task is to use a select statement to return a single column table containing the full title of the person (concatenate all columns together except id), as follows:
** output table schema **
title
*/

SELECT CONCAT(prefix, ' ', first, ' ', last, ' ', suffix) AS title FROM names

-- Alternative solution:

SELECT concat_ws(' ', prefix,first,last,suffix) AS title FROM names

SELECT format('%s %s %s %s', prefix, first, last, suffix) AS title FROM names