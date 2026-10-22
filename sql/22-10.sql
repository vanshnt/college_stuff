create database basicjoin;
use basicjoin;

create table employees(employeeid int primary key, ename varchar(50));

desc employees;

insert into employees values (101, "Vansh"), (102, "Atharv"), (103, "Tanaya"), (104, "Sonal");
insert into employees values (105, "Yash"), (106, "Rohan");
select *from employees;

create table projects(projectid int primary key, pname varchar(50), employeeid int, foreign key(employeeid) references employees(employeeid));

show create table projects;

insert into projects values (01, "E-COM", 101), (02, "Marketing", 102), (03, "Sales", 103), (04, "Survey", 104);

insert into projects values(05, "Customer Service", NULL);



select *from projects;

-- inner join

select *from employees join projects on employees.employeeid = projects.employeeid; 

select e.ename, p.pname from employees e
inner join projects p
on e.employeeid= p.employeeid;

-- right join
select e.ename, p.pname from employees e
right join projects p
on e.employeeid= p.employeeid;


-- left join
select e.ename, p.pname from employees e
left join projects p
on e.employeeid= p.employeeid;



-- outer join
-- display all matching and non matching data for both table

select *from employees 
left join projects
on employees.employeeid = projects.employeeid
union
create database basicjoin;
use basicjoin;

create table employees(employeeid int primary key, ename varchar(50));

desc employees;

insert into employees values (101, "Vansh"), (102, "Atharv"), (103, "Tanaya"), (104, "Sonal");
insert into employees values (105, "Yash"), (106, "Rohan");
select *from employees;

create table projects(projectid int primary key, pname varchar(50), employeeid int, foreign key(employeeid) references employees(employeeid));

show create table projects;

insert into projects values (01, "E-COM", 101), (02, "Marketing", 102), (03, "Sales", 103), (04, "Survey", 104);

insert into projects values(05, "Customer Service", NULL);



select *from projects;

-- inner join

select *from employees join projects on employees.employeeid = projects.employeeid; 

select e.ename, p.pname from employees e
inner join projects p
on e.employeeid= p.employeeid;

-- right join
select e.ename, p.pname from employees e
right join projects p
on e.employeeid= p.employeeid;


-- left join
select e.ename, p.pname from employees e
left join projects p
on e.employeeid= p.employeeid;



-- outer join
-- display all matching and non matching data for both table

select *from employees 
left join projects
on employees.employeeid = projects.employeeid
union
select *from employees
right join projects
on employees.employeeid = projects.employeeid;


select employees.ename, projects.pname from employees
left join projects
on employees.employeeid = projects.employeeid
where projects.employeeid is not null;


select employees.ename, projects.pname from employees
left join projects
on employees.employeeid = projects.employeeid
where projects.employeeid is null;