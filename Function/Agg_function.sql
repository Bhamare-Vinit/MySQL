show databases;
use workbench;
show tables;
select * from student_data;
select * from student_info;

-- The ABS() function returns the absolute (positive) value of a number.
SELECT ABS(-243.5);

-- The AVG() function returns the average value of an expression.
SELECT * FROM student_data
WHERE total_marks > (SELECT AVG(total_marks) FROM student_data);

-- The CEIL() function returns the smallest integer value that is bigger than or equal to a number.
SELECT CEIL(25.75);

-- The COUNT() function returns the number of records returned by a select query.
SELECT COUNT(marks_in_maths) AS NumberOfStudent FROM student_data where total_marks > (SELECT AVG(total_marks) FROM student_data);

-- Return the largest integer value that is less than or equal to 25.75:
SELECT FLOOR(25.75);

-- The GREATEST() function returns the greatest value of the list of arguments.
select greatest(total_marks) from student_data;

-- The GREATEST() function returns the greatest value of the list of arguments.
SELECT name,
       GREATEST(marks_in_maths,marks_in_science,marks_in_english) AS highest_score
FROM student_data;

-- The LEAST() function returns the smallest value of the list of arguments
SELECT name,
       least(marks_in_maths,marks_in_science,marks_in_english) AS highest_score
FROM student_data;

-- The MAX() function returns the maximum value in a set of values.
SELECT MAX(total_marks) AS LargestPrice FROM student_data;
SELECT name ,total_marks
FROM student_data 
WHERE total_marks = (SELECT MAX(total_marks) FROM student_data);

-- The MIN() function returns the minimum value in a set of values.
SELECT name ,total_marks
FROM student_data 
WHERE total_marks = (SELECT min(total_marks) FROM student_data);

-- Return the remainder of 18/4:
SELECT MOD(18, 4);

-- Return 4 raised to the second power:
SELECT POW(4, 2);

-- Return a random decimal number (no seed value - so it returns a completely random number >= 0 and <1):
SELECT RAND();

-- Round the number to 2 decimal places:
SELECT ROUND(135.375, 2);

-- Return the sign of a number:
SELECT SIGN(-12);

-- Return the square root of a number:
SELECT SQRT(64);

-- The SUM() function calculates the sum of a set of values.
SELECT SUM(marks_in_maths) AS Totalmarksmaths FROM student_data;

