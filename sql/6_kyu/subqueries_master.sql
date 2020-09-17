-- Subqueries master
-- 6 kyu

/*
The objective of this Kata is to show that you are proficient at string manipulation (and perhaps that you can use extensively subqueries).

You will use people table but will focus solely on the name column

name
Greyson Tate Lebsack Jr.
Elmore Clementina O'Conner
you will be provided with a full name and you have to return the name in columns as follows.

name	first_lastname	second_lastname
Greyson Tate	Lebsack	Jr.
Elmore	Clementina	O'Conner
Note: Don't forget to remove spaces around names in your result. Note: Due to multicultural context, if full name has more than 3 words, consider first 2 as name
*/

SELECT CASE WHEN LENGTH(name) - LENGTH(replace(name,' ','')) = 3 THEN CONCAT(SPLIT_PART(name, ' ', 1), ' ', SPLIT_PART(name, ' ', 2))
            ELSE SPLIT_PART(name, ' ', 1) END as name,
       CASE WHEN LENGTH(name) - LENGTH(replace(name,' ','')) = 3 THEN SPLIT_PART(name, ' ', 3)
            ELSE SPLIT_PART(name, ' ', 2) END as first_lastname,
       CASE WHEN LENGTH(name) - LENGTH(replace(name,' ','')) = 3 THEN SPLIT_PART(name, ' ', 4)
             ELSE SPLIT_PART(name, ' ', 3) END as second_lastname
FROM people