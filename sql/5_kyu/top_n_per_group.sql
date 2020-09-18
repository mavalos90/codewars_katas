-- Using Window Functions To Get Top N per Group
-- 5 kyu

/*
Description
Given the schema presented below write a query, which uses a window function, that returns two most viewed posts for every category.

Order the result set by:

category name alphabetically
number of post views largest to lowest
post id lowest to largest
Note:
Some categories may have less than two or no posts at all.
Two or more posts within the category can be tied by (have the same) the number of views. Use post id as a tie breaker - a post with a lower id gets a higher rank.
Schema
categories
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
id          | integer                     | not null
category    | character varying(255)      | not null
posts
 Column     | Type                        | Modifiers
------------+-----------------------------+----------
id          | integer                     | not null
category_id | integer                     | not null
title       | character varying(255)      | not null
views       | integer                     | not null
Desired Output
The desired output should look like this:

category_id | category | title                             | views | post_id
------------+----------+-----------------------------------+-------+--------
5           | art      | Most viewed post about Art        | 9234  | 234
5           | art      | Second most viewed post about Art | 9234  | 712
2           | business | NULL                              | NULL  | NULL
7           | sport    | Most viewed post about Sport      | 10    | 126
...
category_id - category id
category - category name
title - post title
views - the number of post views
post_id - post id
*/

WITH ranks AS (
  Select 
       c.id as category_id,
       c.category,
       p.title,
       p.views,
       p.id as post_id,
       row_number() over (partition by c.id order by p.views desc, p.id ASC) as rank 
    FROM posts p
    FULL JOIN categories c
    ON c.id = p.category_id)
SELECT category_id,
       category,
       title,
       views,
       post_id
FROM ranks
where rank <= 2
ORDER BY category ASC, views DESC, post_id ASC