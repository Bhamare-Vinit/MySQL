
-- Return the current date:
-- This function equals the CURRENT_DATE() function.
SELECT CURDATE();

-- The CURRENT_TIME() function returns the current time.
-- Note: The time is returned as "HH-MM-SS" (string) or as HHMMSS.uuuuuu (numeric).
-- Note: This function equals the CURTIME() function.
SELECT CURRENT_TIME();

-- The CURRENT_TIMESTAMP() function returns the current date and time.
-- Note: The date and time is returned as "YYYY-MM-DD HH-MM-SS" (string) or as YYYYMMDDHHMMSS.uuuuuu (numeric).
SELECT CURRENT_TIMESTAMP();

-- The DATE() function extracts the date part from a datetime expression.
SELECT DATE("The date is 2017-06-15");

-- Return the number of days between two date values:
SELECT DATEDIFF("2017-06-25", "2017-06-15");

-- The DATE_FORMAT() function formats a date as specified.
SELECT DATE_FORMAT("2017-06-15", "%W %M %e %Y");

-- Return the day of the month for a date:
SELECT DAY("2017-06-15");

-- Return the weekday name for a date:
SELECT DAYNAME("2024-07-30");

-- The EXTRACT() function extracts a part from a given date.
SELECT EXTRACT(WEEK FROM "2017-06-15");


-- Return current date and time:
SELECT LOCALTIME();




