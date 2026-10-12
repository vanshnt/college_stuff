create database CompanyDB;
show databases;
create table Employees(EmpID int primary key,EmpName varchar(30), Salary int, JoinDate date);
desc Employees;
create table Departments(DeptID int primary key,DeptName varchar(30));

desc Departments;

alter table Employees add (Email varchar(30));
desc Employees;

alter table Departments add (dept_location varchar(30));
desc Departments;


alter table Employees add(Phone int(13));

alter table Employees modify phone int not null;

alter table Employees modify EmpName  varchar(100);
desc Employees;

alter table Departments drop primary key;
desc Departments;
alter table Employees add (DeptID int);

ALTER TABLE Departments
ADD PRIMARY KEY (DeptID);

Alter table Employees add constraint FK_Staff_Department 
foreign key(DeptID) references Departments(DeptID);
desc Employees;

alter table Employees rename column EmpName to EmployeeName;
desc Employees;

alter table Employees add (Age int);
alter table Employees add constraint check_empAge_Salary check (Age >=21 and Salary >=10000);

alter table Employees drop column Phone;
desc Employees;

rename table Employees to EmployeeDetails;
desc EmployeeDetails;

alter table EmployeeDetails drop check check_empAge_Salary;

alter table EmployeeDetails drop foreign key FK_Staff_Department;
drop table Departments;

drop database CompanyDB;