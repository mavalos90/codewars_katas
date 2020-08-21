/*
SQL Basics: Top 10 customers by total payment amount
6 kyu


For this kata we will be using the DVD Rental database.
Your are working for a company that wants to reward its top 10 customers with a free gift. You have been asked to generate a simple report that returns the top 10 customers by total amount spent. Total number of payments has also been requested.
The query should output the following columns:

customer_id [int4]
email [varchar]
payments_count [int]
total_amount [float]
and has the following requirements:

only returns the 10 top customers, ordered by total amount spent.
*/

SELECT 
    c.customer_id, 
    c.email,
    COUNT(payment_id) AS payments_count, 
    SUM(amount)::float AS total_amount
FROM 
    payment p 
JOIN 
    customer c
ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.email
ORDER BY SUM(amount) DESC
LIMIT 10;