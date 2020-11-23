-- Present JSON data the SQL way
-- 6 kyu

/*
Task
Given the database where users are stored in JSON format, fetch the records splitting the data into separate columns.

Notes
The private field determines whether the user's email address should be publicly visible
If the profile is private, email_address should equal "Hidden"
The users may have multiple email addresses
If no email addresses are provided, email_address should equal "None"
If there're multiple email addresses, the first one should be shown
The date_of_birth is in the yyyy-mm-dd format
The age fields represents the user's age in years
Order the result by the first_name, and last_name columns
*/

SELECT data ->> 'first_name' AS first_name,
       data ->> 'last_name' AS last_name,
       EXTRACT(YEAR from AGE(to_date(data ->> 'date_of_birth', 'yyyy-mm-dd')))::integer AS age,
       CASE
          WHEN data->>'private' = 'true' THEN 'Hidden'
          WHEN data->>'private' = 'false' AND data#>>'{email_addresses, 0}' IS null THEN 'None'
      ELSE data#>>'{email_addresses, 0}'
      END AS email_address
FROM users
ORDER BY first_name, last_name