-- database :  CREATE DATABASE name ; 
-- TABLE :  create table EMP
-- INSERT INTO EMP VALUES 
/*
1. =    ---> where department ='IT'
2. > , < , >= <= ,<> (not equal to) ---> salary col 
3. AND operator  : IT work and  salary above 50000
4. OR   : work  in hr or IT.
5. not  : not in ahmedabad
6.between : salary between 30000-50000
7. IN ,  NOT IN : IN("IT","HR")
8. like : person name  start with p ----> like p%
9. concatenation operator : use  concat()

*/
CREATE database SQL_MOR;

USE SQL_MOR;
create table EMP (
	id INT,
    first_name varchar(30),
    last_name varchar(30),
    department varchar(30),
    salary INT,
    city varchar(30)
);

INSERT INTO EMP VALUES
(101,'Amit','Patel','IT',55000,'Ahmedabad'),
(102,'Priya','Sharma','HR',45000,'Surat'),
(103,'Rahul','Mehta','Finance',65000,'Vadodara'),
(104,'Neha','Joshi','IT',70000,'Rajkot'),
(105,'Riya','Shah','Sales',50000,'Ahmedabad');

select * from EMP; 

-- where   -----> condition 

-- 1.print  only those  employees name, work in IT department . 
select first_name, department  from EMP where department ='IT';

-- 2. print only those  employees name live in ahmedabad.
select first_name, city  from EMP where city ='Ahmedabad';

-- 3. print only those  emp salary is greater than 30000 . 
select first_name,last_name,salary from  emp where salary >30000;
select first_name,last_name,salary from  emp where salary <50000;
select first_name,last_name,salary from  emp where salary >=45000;
select first_name,last_name,salary from  emp where salary <=55000;

select first_name,last_name,salary from  emp where salary !=50000;  -- !=  not equal to  

-- 4. AND operator  :  print emp  salary >55000 and  work in IT
select first_name , department ,salary 
from emp 
where department='IT' 
AND 
salary >55000;

-- 5 OR operator  :  print emp live in ahmedabad , salary >70000 
select  first_name , salary , city 
from emp 
where city ="Ahmedabad" 
or 
salary >70000;

-- 6 between salary 30000 -50000 
select  first_name , salary , city 
from emp 
where salary between  55000 and 70000;

 -- 7. IN  : print  emp name  who  work  IT and  HR
 
select first_name,salary ,department
from emp 
where department IN('IT','HR');

-- 8. print emp name who start with 'r' . , _ 

select first_name , salary 
from emp 
where first_name like '%a'; -- note : start P% means  start with p letter , %p end with p letter.

-- concat() , || 
select concat(first_name," ",last_name) as full_name from emp;