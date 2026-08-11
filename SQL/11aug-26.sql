use scott;

select * from employees;

-- print employees name  who's  hire in  jan , june ,july 

select first_name , hire_date 
from employees 
where MONTH(hire_date) 
in (1,6,7);

-- print first  5  rows only  function  ----> limit 

select *  from  employees limit 5; 

-- print only those  employees who  work in IT_PROG and Salary  is greater than  6000 print  only 3 rows.

/*
order by  
limit  
is not null 
is null
*/

-- sort  ---->  asc desc   desc to  asc  ----> function  : order by 

-- ex :1  salary  sort asc to  desc 
select first_name ,salary from employees order by salary asc;

-- ex :2  salary  desc to asc 
select first_name ,salary from employees order by salary desc;

-- ex :3 using column number 
select * from  employees order by 8 desc;

-- ex :4 
select first_name ,salary  
from employees 
order by 
first_name asc ,salary asc;

-- ex :5 
select first_name ,salary  
from employees 
order by 
1,2;

 -- is null : print  null value 

select first_name ,commission_pct 
from employees 
where commission_pct is not null;

select first_name ,commission_pct 
from employees 
where commission_pct is null
order by 1;


select max(salary) from employees;
select min(salary) from employees;
select avg(salary) from employees;




