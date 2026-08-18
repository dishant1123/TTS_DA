use scott; 

select * from employees; 

/*
having  :  select  ..... from table  name  where  ..... group by   .... having (agg fuction)

1.Department-wise total salary > 50,000

2.Department-wise average salary > 7,500

3.Departments having more than 5 employees

4.Job-wise total salary > 20,000

5.Job-wise average salary < 8,000

6.Department-wise minimum salary > 3,000

7.Department-wise maximum salary > 10,000

8.Job-wise employee count at least 3

9.Department-wise total salary and employee count

 Conditions:

Total salary > 50,000
Employee count > 3

10.Job-wise average salary between 5,000 and 10,000

11.Department-wise total salary > 30,000 and employees > 2

12.Department-wise average salary > 6,000 and maximum salary > 10,000

13.Job-wise total salary for selected jobs

Jobs:

IT_PROG
ST_CLERK
AD_VP
SA_REP
*/

-- 1 . Department-wise total salary > 50,000
select department_id ,sum(salary) as depart_salary 
from 
employees 
group by department_id
having sum(salary) > 5000;

-- 2.Department-wise average salary > 7,500
select department_id ,avg(salary) as depart_salary 
from 
employees 
group by department_id
having avg(salary) > 7500;

-- 3.Departments having more than 5 employees
select  department_id, count(*) as employess_count 
from employees 
group by department_id 
having count(*) >=2; 

-- 4 Job-wise total salary > 20,000  raju 
select job_id, sum(salary) as total_job_id_salary
from employees 
group by job_id 
having sum(salary) > 20000;

-- 5.Job-wise average salary < 8,000  jay 
select job_id, avg(salary) as total_job_id_avg_salary
from employees 
group by job_id 
having avg(salary) < 8000;

-- 6.Department-wise minimum salary > 3,000  varun 
select department_id , min(salary) 
from  employees 
group by department_id
having min(salary) > 3000;

-- 7.Department-wise maximum salary > 10,000 shrutika 
select department_id , max(salary) 
from  employees 
group by department_id
having max(salary) > 10000;

-- 8.Job-wise employee count at least 3

select  job_id, count(*) as employess_count 
from employees 
group by  job_id
having count(*) >=3; 

-- 9
/*
9.Department-wise total salary and employee count
Conditions:
Total salary > 50,000
Employee count > 3
*/

select department_id , sum(salary) as total_salary ,
count(*) as employess_count 
from employees 
group by department_id 
having sum(salary) >10000 
and count(*) > 3 ; 

-- 10.Job-wise average salary between 5,000 and 10,000
 
select job_id ,avg(salary) as avg_salary 
from employees 
group by job_id
having avg(salary) between 5000 and 10000; 
