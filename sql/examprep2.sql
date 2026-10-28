set sql_safe_updates = 0;
create database trainingcenter;
use trainingcenter;
create table course(course_id int primary key, course_name varchar(30), duration int, fees int);
create table student(student_id int, student_name varchar(30), dob date, city varchar(30), course_id int, marks int);
create table trainer(trainer_id int, trainer_name varchar(30), specialization varchar(30), experience int);


alter table student add primary key(student_id);
desc trainer;
alter table trainer add primary key(trainer_id);


INSERT INTO course VALUES
(1, 'Python', 3, 8000),
(2, 'Web Development', 6, 15000),
(3, 'Data Science', 8, 25000),
(4, 'Java', 4, 12000),
(5, 'SQL', 2, 5000);

INSERT INTO student VALUES
(101, 'Vansh', '2004-05-15', 'Pune', 1, 85),
(102, 'Atharv', '2003-08-20', 'Mumbai', 2, 78),
(103, 'Tanaya', '2004-01-10', 'Kolhapur', 3, 92),
(104, 'Sonal', '2003-11-25', 'Pune', 5, 67),
(105, 'Rohan', '2004-07-05', 'Delhi', 4, 74);

INSERT INTO trainer VALUES
(201, 'Amit Sharma', 'Python', 5),
(202, 'Neha Patil', 'Web Development', 7),
(203, 'Raj Mehta', 'Data Science', 10),
(204, 'Priya Shah', 'Java', 4),
(205, 'Karan Joshi', 'SQL', 6);


alter table course add constraint chk_fees check (fees >= 5000);
alter table student add constraint chk_marks check (marks between 0 and 100);

alter table student add column guardian_name varchar(30);

alter table trainer modify specialization varchar(100);

alter table course add constraint unique(course_name);

alter table student add constraint fk_student_course
foreign key(course_id) references course(course_id);
show create table student;

update course set fees = 18000 where course_name = "Python";
update course set duration = duration+1;
select *from course;

update student set city = "Nasik" where student_id = 105;

delete from student where marks <70;
alter table student drop column guardian_name;
rename table trainer to faculty;
alter table student drop constraint chk_marks;

select *from student;

truncate table faculty;
alter table student drop constraint fk_student_course;
drop table course;
drop table student;
drop table faculty;








CREATE TABLE Office (
    office_id INT PRIMARY KEY,
    office_name VARCHAR(50),
    city VARCHAR(30)
);

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(30),
    salary INT,
    office_id INT,
    CONSTRAINT fk_office
        FOREIGN KEY (office_id)
        REFERENCES Office(office_id)
);



-- 1. Insert into Office
INSERT INTO Office VALUES
(4, 'Marketing', 'Pune'),
(5, 'Development', 'Mumbai'),
(6, 'Support', 'Kolhapur');

-- 2. Insert into Employee
INSERT INTO Employee VALUES
(105, 'Rahul', 32000, 4),
(106, 'Priya', 42000, 5),
(107, 'Rohan', 28000, 6);

delete e from employee e
inner join office o
on e.office_id = o.office_id
where city = "Pune";

select *from employee;