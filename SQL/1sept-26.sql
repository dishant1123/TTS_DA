/*
1. Employees earning more than average salary
2. Employee(s) earning the highest salary 
3.Employee(s) earning the lowest salary
4.Employees earning more than employee 103 
5.Employees working in the same department as employee 103 
6. Employees working in departments where someone earns more than 8000 
7.Display employees who work in the department having the highest average salary. 
8.Departments having average salary greater than 5000
*/ 
-- sub query  : 

-- 1. Employees earning more than average salary
select first_name ,
salary from 
employees where salary > 
(
select avg(salary) as avg_salary_emp 
from 
employees);

-- 2. Employee(s) earning the highest salary.

select first_name ,salary 
from  employees 
where salary  = (
select max(salary) as highest_salary 
from employees
);

-- 3.Employee(s) earning the lowest salary
select first_name ,salary 
from  employees 
where salary  = (
select min(salary) as lowest_salary 
from employees
);

-- 4.Employees earning more than employee 103
select employee_id ,first_name ,salary,department_id from employees; 
select first_name , salary  
from employees 
where salary >
(select salary from employees where  employee_id =103);  

-- 5.Employees working in the same department as employee 103 

select employee_id ,first_name ,department_id 
from employees 
where department_id = (
select department_id from employees 
where employee_id =103
);

-- 6. Employees working in departments where someone earns more than 8000 
select FIRST_NAME , salary ,DEPARTMENT_ID 
from employees 
where department_id IN 
(select department_id  
from 
employees
where salary > 8000);

-- 7.Display employees who work in the department having the highest average salary. 
-- 8.Departments having average salary greater than 5000