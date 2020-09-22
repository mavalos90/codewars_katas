-- Relational division: Find all movies two actors cast in together
-- 5 kyu
/*
Given film_actor and film tables from the DVD Rental sample database find all movies both Sidney Crowe (actor_id = 105) and Salma Nolte (actor_id = 122) cast in together and order the result set alphabetically.

film schema
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
title       | character varying(255)      | not null
film_id     | smallint                    | not null
film_actor schema
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | smallint                    | not null
film_id     | smallint                    | not null
last_update | timestamp without time zone | not null 
actor schema
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | integer                     | not null 
first_name  | character varying(45)       | not null
last_name   | character varying(45)       | not null
last_update | timestamp without time zone | not null 
The desired output:

title
-------------
Film Title 1
Film Title 2
...
*/


With intersect:
SELECT title
    FROM film_actor
    INNER JOIN film 
    USING (film_id)
    WHERE actor_id = 105
INTERSECT 
SELECT title
    FROM film_actor
    INNER JOIN film 
    USING (film_id)
    WHERE actor_id = 122

Scalable solution with more actors:

SELECT f.title
  FROM film f
  JOIN film_actor fa ON fa.film_id = f.film_id
  WHERE fa.actor_id IN (105,122)
  GROUP BY f.film_id
  HAVING COUNT(*) = 2
ORDER BY f.title ASC

