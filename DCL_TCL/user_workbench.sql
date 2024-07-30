show databases;
use workbench;
show tables;
select * from student_data;
select * from student_info;

-- following command denied for user vinit user only have access to see tables
INSERT INTO student_data (roll_number, name, marks_in_maths, marks_in_science,marks_in_english)
VALUES (4, 'Shreyas', 75, 82, 55);




