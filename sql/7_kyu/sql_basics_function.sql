-- SQL Basics: Create a FUNCTION
-- 7 kyu

-- For this challenge you need to create a basic Increment function which Increments on the age field of the peoples table.
-- The function should be called increment, it needs to take 1 integer and increment that number by 1.
-- Your solution should use PL/SQL

CREATE FUNCTION increment(val integer) RETURNS integer AS $$
BEGIN
    RETURN val + 1;
END; $$
LANGUAGE PLPGSQL;