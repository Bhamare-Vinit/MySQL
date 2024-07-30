show databases;
use workbench;
show tables;
select * from student_data;
select * from student_info;
CREATE USER 'vinit'@'localhost' IDENTIFIED BY 'Vinit@2002';

GRANT SELECT ON workbench.* TO 'vinit'@'localhost';
SHOW GRANTS FOR 'vinit'@'localhost';
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'vinit'@'localhost';

REVOKE ALL PRIVILEGES ON workbench.* FROM 'vinit'@'localhost';


