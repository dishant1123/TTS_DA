/*
1.Display employee name and manager name

2.Display employee name, employee ID and manager name

3.Display employee name, salary and manager name  hw
4.Display employee name, manager name and manager salary hw 

5. Display employees whose manager is Steven

6.Display employees whose salary is greater than their manager's salary
7.Display only employees who don't have a manager

8.Display manager name and number of employees working under each manager  ---> self join +group by

9.Display all employees and all departments, including unmatched 
records ----> full  outer join  ----> use 
10.Display employees who don't belong to any department and 
departments that don't have any employee.

11.Display every employee with the IT and Sales departments.
*/ 

use scott;
select * from  employees; 
-- 1.Display employee name and manager name

select e.first_name  as employees_name, 
m.first_name as manager_name 
from employees e 
join employees m 
on e.manager_id = m.employee_id;

-- 2.Display employee name, employee ID and manager name

select e.first_name  as employees_name, 
m.first_name as manager_name ,
e.employee_id as id 
from employees e 
join employees m 
on e.manager_id = m.employee_id;

-- 5.Display employees whose manager is Steven 
select e.first_name  as employees_name, 
m.first_name as manager_name 
from employees e 
join employees m 
on e.manager_id = m.employee_id
where m.first_name ="Steven";

-- 6.Display employees whose salary is greater 
-- than their manager's salary

select e.first_name  as employees_name, 
m.first_name as manager_name ,
e.salary as employees_salary , 
m.salary as manager_salary
from employees e 
join employees m 
on e.manager_id = m.employee_id
where e.salary > m.salary;

-- 7.Display only employees who don't have a manager
select employee_id ,manager_id ,first_name
from employees;

select e.first_name as emp_name , 
m.manager_id as m_id2
from employees e 
left join employees m 
on e.manager_id = m.employee_id 
where m.employee_id is null; 

