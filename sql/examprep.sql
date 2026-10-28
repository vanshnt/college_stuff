create database exam;
use exam;
create table employee(
eid int,
ename varchar(30),
ebranch varchar(40));

show create table employee;
desc employee;

alter table employee add column phone_no float;
alter table employee modify ename varchar(100);
alter table employee rename column ebranch to emp_branch;
alter table employee drop column phone_no;
alter table employees add column age int;
rename table employee to employees;

drop table employees;

-- constraints
desc employees;
alter table employees add primary key(eid);
alter table employees drop primary key;

alter table employees add constraint chk_age check (age>=18);
alter table employees drop constraint chk_age;
insert into employees values(01, "Vansh", "Pune", 15);
insert into employees values(02, "Vansh", "Pune", 19);
truncate table employees;
select *from employees;


alter table employees add (office_id int, role varchar(40));

-- foreign key

create table office(office_id int primary key);

alter table employees 
add constraint fk_office_employee
foreign key (office_id) references office(office_id);

show create table employees;

alter table employees drop foreign key fk_office_employee;


-- insert update delete
select *from employees;
ALTER TABLE employees
ADD PRIMARY KEY (eid);
insert into employees values(01, "Vansh", "Pune", 21, 01, "Dev"), (02, "Atharv", "Pune", 22, 01, "Manager");

update employees set emp_branch = "Kolhapur" where eid = 2;
delete from employees where eid = 2;

INSERT INTO Employees
VALUES
(2, 'Atharv', 'Mumbai', 22, 2, 'Tester'),
(3, 'Tanaya', 'Pune', 23, 1, 'Manager'),
(4, 'Sonal', 'Kolhapur', 24, 3, 'HR'),
(5, 'Yash', 'Mumbai', 21, 2, 'Dev'),
(6, 'Rohan', 'Delhi', 25, 4, 'Analyst'),
(7, 'Priya', 'Pune', 22, 1, 'Tester'),
(8, 'Aarav', 'Kolhapur', 26, 3, 'Manager'),
(9, 'Sneha', 'Delhi', 23, 4, 'HR'),
(10, 'Rahul', 'Mumbai', 27, 2, 'Dev');


select *from employees where age>22;
select *from employees where emp_branch = "Pune";
select *from employees where age between 21 and 24;
select *from employees where emp_branch = "Pune" and role = "Dev";
select *from employees where emp_branch in ("Mumbai", "Delhi");
select *from employees where role != "Dev";
select *from employees where office_id in(1,3);

select *from employees where ename like 'V%';
select *from employees where ename like '%a%';


-- Sort
select *from employees order by emp_branch;
select *from employees order by emp_branch desc;
select *from employees order by emp_branch limit 5;


-- joins
drop table office;

CREATE TABLE Office (
    office_id INT PRIMARY KEY,
    office_name VARCHAR(50),
    office_city VARCHAR(50)
);
INSERT INTO Office VALUES
(1, 'IT Department', 'Pune'),
(2, 'Development', 'Mumbai'),
(3, 'HR Department', 'Kolhapur'),
(4, 'Analytics', 'Delhi'),
(5, 'Finance', 'Nashik'),
(6, 'Marketing', 'Bangalore');


-- inner join
SELECT e.ename, o.office_name
FROM employees e
INNER JOIN Office o
ON e.office_id = o.office_id;


select e.ename, o.office_id
from employees e
inner join office o
on e.office_id = o.office_id;

INSERT INTO Employees
VALUES
(11, 'Atharv', 'Mumbai', 22, Null, 'Tester');


-- left join
select e.ename, o.office_id
from employees e
left join office o
on e.office_id = o.office_id;

-- right join
select e.ename, o.office_id
from employees e
right join office o
on e.office_id = o.office_id;

-- outer join

select e.ename, o.office_id
from employees e
left join office o
on e.office_id = o.office_id
union
select e.ename, o.office_id
from employees e
right join office o
on e.office_id = o.office_id;

-- aggregate functions
select count(*) from employees;
select count(*) from employees where emp_branch = "Pune";
select max(eid) from employees;

select sum(eid) as total from employees;
select count(distinct emp_branch) as city from employees;


-- group by and having
select *from employees;
select office_id, count(*) as employee_count from employees group by office_id;


-- single row functions

select upper(ename) as name, lower(emp_branch) as city from employees;

select CONCAT(ename, " ", emp_branch) as info from employees;
select substr(ename, 1, 3) from employees;
select instr(ename, "a") as position from employees;




