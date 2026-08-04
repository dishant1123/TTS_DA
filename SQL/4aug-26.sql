-- create DATABASE mor_TTS;
-- use mor_TTS;
-- select , from , col_rename ,  create database ,create table ,insert value , aithematic operator , power function

use employees;

select * from emp;

/*
	select ====> function  
    *      ====> whole data  total data to print 
    from   ====> function   ---> data get , fetch 
    emp    =====> table name  
*/

-- print name  and salary  . 
select name,salary from emp; -- select col_name1,col_name2  from table_name ;

-- print only name .
select name from emp;  

-- print only salary 
select salary from emp;

-- rename salary  to  first_salary 
select salary as first_salary from emp;
select * from emp;

-- print annual salary  
select name , salary,salary*12 as annual_salary from emp;

-- print salary +1200 bonus   print  both  salary and bonus_add salary 
select salary,salary+1200 as bonus_add_salary from emp;

-- printname ,salary , bonus 1200 , 6 month salary , 12 month salary ,  qtrwise salary 
/* display like  
name  salary  bonus   6month   12month  permonth   Qtr wise
jay    30000   31200   180000   360000   30000      

*/
select name, salary, salary+1200 as bonus_salary,
salary*6 as half_mon, 
salary*12 as yr_wise, 
salary*3 as qtr_wise 
from emp;

use deyaan_sql;

select * from orders;

-- print customer_id ,payment_mode ,city  
select customer_id , payment_mode ,city from orders;

-- print order_id ,city 
select order_id , city from orders;

select * from customers;


