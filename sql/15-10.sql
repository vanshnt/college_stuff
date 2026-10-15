create database user;
use user;
show databases;

create table customer(cusID int,
custName varchar(30),
city varchar(10),
product varchar (40),
price int);

desc customer;

insert into customer values (101, "Vansh", "Pune", "Laptop", 50000), (102, "Atharv", "Pune", "PC", 50000), (103, "yash", "Pune", "Smartphone", 50000); 

alter table customer add primary key(cusID);


select cusID, custName, city from customer;

select *from customer where cusID in (101, 103) ;

create table cloneTable as select *from customer;

select *from cloneTable;
drop table CloneTable;

insert into customer values (104, "Rohan", "Pune", "Tablet", 20000), (105, "Sonal", "Pune", "Ipad", 15000), (106, "Nisha", "Pune", "macbook", 90000); 

select custName, product, price from customer where price > 30000;
insert into customer values (107, "Karan", "Kolhapur", "Smartphone", 35000);
select custName, city from customer where city = "Kolhapur";
insert into customer values (108, "Ishwar", "Kolhapur", "Iphone", 75000);
select *from customer order by price desc;

# sorting data order by multiple column 

select * from customer order by city, price desc;

select * from customer order by city desc, price asc;


#	Single row function 
# 	case conversion function

select upper(custName), lower(product) from customer
where cusID<103;


alter table customer add column lastName varchar(30);

update customer set lastName = "Bijwani" where cusID = 101;
update customer set lastName = "Dugani" where cusID = 102;

select *from customer;
select concat(custName," ", lastName) as FullName from customer;



# use of substr and instr functions

select * from customer;
select substr(custName, 1, 3) from customer;

select substr(custName, 0, 3) from customer;
select substr(custName, 1, 5) from customer;

select instr(custName, "a") as position from customer;

select substr(custName, 1, 3), instr(custName, "a") from customer where cusID <105;