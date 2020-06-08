-- Adults only (SQL for Beginners #1)
-- 8 kyu

-- In your application, there is a section for adults only. You need to get a list of names and ages of users from the users table, who are 18 years old or older.
-- users table schema
-- name
-- age

SELECT name, age
FROM users
WHERE age >= 18;