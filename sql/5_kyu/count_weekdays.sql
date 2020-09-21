-- Count Weekdays
-- 5 kyu

/*
You need to create a function that calculates the number of weekdays (Monday through Friday) between two dates inclusively.

The function should be named weekdays accept two arguments of type DATE and return an INTEGER value.

weekdays(DATE, DATE) INTEGER
The order of arguments shouldn't matter. To illustrate both of the following queries

SELECT weekdays('2016-01-01', '2016-01-10');
SELECT weekdays('2016-01-10', '2016-01-01');
should produce the same result

 weekdays
----------
        6
*/

CREATE FUNCTION weekdays(date, date)
  RETURNS integer
  LANGUAGE plpgsql
  AS
$func$
DECLARE
   d        date := LEAST($1, $2);
   weekdays int  := 0;
BEGIN
   LOOP
      IF extract(isodow from d) < 6 THEN
         weekdays := weekdays + 1;
      END IF;
      d := d + 1;
      EXIT WHEN d > GREATEST($1, $2);
   END LOOP;
   RETURN weekdays;
END
$func$