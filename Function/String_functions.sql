show databases;
use workbench;
show tables;
select * from student_data;
select * from student_info;

-- Required. The character to return the ASCII value for. If more than one character is entered, it will only return the value for the first character
SELECT name, ASCII(name) AS NumCodeOfFirstChar
FROM student_data;

-- The CHAR_LENGTH() function return the length of a string (in characters).
SELECT name, CHAR_LENGTH(name) AS LengthOfName
FROM student_data;

-- The CONCAT() function adds two or more expressions together.
SELECT name, CONCAT("Department: ", department, ", Grade: ", grade) AS report
FROM student_info;

-- The INSTR() function returns the position of the first occurrence of a string in another string.
SELECT INSTR(name, "it")
FROM student_info;

-- The LCASE() function converts a string to lower-case.
SELECT name,LCASE(grade) AS LowercaseCustomerName
FROM student_info;

-- The LEFT() function extracts a number of characters from a string (starting from left).
SELECT name,LEFT(name, 4) AS ExtractString
FROM student_data;

-- The LENGTH() function returns the length of a string (in bytes).
SELECT name,LENGTH(name) AS LengthOfName
FROM student_data;

-- The LOCATE() function returns the position of the first occurrence of a substring in a string.
-- If the substring is not found within the original string, this function returns 0.
-- This function performs a case-insensitive search.
SELECT LOCATE("vinit", name)
FROM student_data;

-- The LOWER() function converts a string to lower-case.
SELECT LOWER(grade) AS LowercaseCustomerName
FROM student_info;

-- The LPAD() function left-pads a string with another string, to a certain length.
SELECT LPAD(name, 30, "sir ") AS LeftPadCustomerName
FROM student_data;


SELECT MID(name, 2, 3) AS ExtractString
FROM student_data;

-- The REPEAT() function repeats a string as many times as specified.
SELECT name,REPEAT(grade, 2) as repeatGrade
FROM student_info;

SELECT name,replace(name,"it","u")as replacename
FROM student_info;


SELECT REVERSE(name)
FROM student_data;

-- The RIGHT() function extracts a number of characters from a string (starting from right).
SELECT name,RIGHT(name, 5) AS ExtractString
FROM student_data;

-- The SUBSTR() function extracts a substring from a string (starting at any position).
SELECT SUBSTR(name, 2, 5) AS ExtractString
FROM student_data;

