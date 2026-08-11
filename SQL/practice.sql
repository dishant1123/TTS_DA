use mor_tts;

create table employee(
	id int,
    first_name varchar(30),
    last_name  varchar(30),
    department varchar(30),
    salary int,
    city varchar(30)
    
);

INSERT INTO employee VALUES
(101,'Amit','Patel','IT',55000,'Ahmedabad'),
(102,'Priya','Sharma','HR',45000,'Surat'),
(103,'Rahul','Mehta','Finance',65000,'Vadodara'),
(104,'Neha','Joshi','IT',70000,'Rajkot'),
(105,'Riya','Shah','Sales',50000,'Ahmedabad');

select * from employee;



select  concat(first_name," ",last_name) from employee;

use scott;
select * from employees;

select * from employees where manager_id IN(100 , 124 , 149);
select * from employees where department_id not in (90 , 110 , 10); 

SELECT last_name, department_id, job_id
FROM employees
WHERE (department_id, job_id) IN
(
    (50,'ST_CLERK'),
    (80,'SA_REP')
);

select * from employees limit 5; 

select * from  employees order by salary desc;
select * from  employees order by 8 desc;

select first_name ,commission_pct from employees where commission_pct is not null;
SELECT *
FROM employees
WHERE MONTH(hire_date) IN (1,6,7);
/*
order by  
limit  
is not null 
is null
*/
select * from employees where MANAGER_ID IN (100 , 124,149);
-- 8 DISPLAY THOSE WHOSE (DEPARTMENT_ID,MANAGER_ID,JOB_ID) ARE 50,124,ST_CLERK   60,103,IT_PROG    90,100,AD_VP . 


select * from employees where 
(department_id =50 and manager_id=124 and job_id="ST_CLERK") 
or 
(department_id =60 and manager_id=103 and job_id="IT_PROG") 
or 
(department_id =90 and manager_id=100 and job_id="AD_VP"); 

select first_name,department_id,manager_id,job_id
from employees 
where (department_id,manager_id,job_id) 
IN 
(
	(50,124,'ST_CLERK'),
    (60,103,'IT_PROG'),
    (90,100,'AD_VP')
);

-- like : 
select first_name from employees where first_name like '%p%' ;

select * from employees; 
