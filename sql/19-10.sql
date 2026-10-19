use college;

select now();

select now() as currentTime;

create table student(rollno int, name varchar(30), city varchar(30), course varchar(30));

alter table student add Today_date date;

desc student;

INSERT INTO student VALUES
(1, 'Vansh', 'Pune', 'MCA', CURDATE()),
(2, 'Atharv', 'Pune', 'MCA', CURDATE()),
(3, 'Yash', 'Kolhapur', 'BCA', CURDATE()),
(4, 'Rahul', 'Mumbai', 'MCA', CURDATE());





create database organization;

use organization;
desc employee;
create table employee(EmpID int not null primary key, first_name varchar(30), Last_name varchar(30), gender char, role varchar(30), dept varchar(30), manager_id varchar(30));

INSERT INTO employee VALUES
(101, 'Vansh', 'Bijwani', 'M', 'Manager', 'HQ', 'M11'),
(102, 'Atharv', 'Dugani', 'M', 'Developer', 'IT', 'M12'),
(103, 'Yash', 'Patil', 'M', 'Accountant', 'Finance', 'M13'),
(104, 'Priya', 'Sharma', 'F', 'Recruiter', 'HR', 'M14'),
(105, 'Sneha', 'Joshi', 'F', 'Designer', 'Marketing', 'M15'),
(106, 'Rahul', 'Kadam', 'M', 'Sales Executive', 'Sales', 'M16');



-- distinct keyword
-- Distinct keyword for unique data
select distinct dept from employee order by Dept;

select distinct role from employee order by role;


-- and operator is logical operator that carries two or more boolean expression

select *from employee where role = "Manager" and dept = "HQ";


-- Or operator is same as and it only return false if both conditions are false

select *from employee where role = "Developer" or EmpID = 102;


--  IN operator
select *from employee where role in ("Accountant", "Designer");

select *from employee where role not in ("Accountant", "Designer");



alter table employee add experience int;

update employee set experience = 10 where EmpID = 101;
update employee set experience = 20 where EmpID = 102;
update employee set experience = 18 where EmpID = 103;
update employee set experience = 6 where EmpID = 104;
update employee set experience = 2 where EmpID = 105;
update employee set experience = 18 where EmpID = 106;


select *from employee where experience between 10 and 20;
select *from employee where experience = 10 or experience = 20;



-- Like Operator 

select * from employee where last_name like "%a%";

