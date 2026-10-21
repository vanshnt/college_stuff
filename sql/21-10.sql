use organization;
select *from employee;

select count(*)from employee where dept = "Sales";
select min(experience) from employee;
select max(experience) from employee;
select sum(experience) from employee;
select avg(experience) as emp_exr from employee;

select dept, count(*) as employee_count from employee group by dept;

select role, count(*) as employee_count from employee group by role;
select gender, count(*) as employee_count from employee group by gender;

select dept, sum(experience) as total_experience
from employee group by dept
having total_experience >= 10 and total_experience <= 20;


select dept, sum(experience) as total_experience
from employee group by dept
having total_experience >= 10 or total_experience <= 20;