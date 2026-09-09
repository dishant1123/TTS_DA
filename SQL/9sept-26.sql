use scott;

select * from employees; 
select * from  departments;
/* 
1.Display employee name and manager name

2.Display employee name, employee ID and manager name

3.Display employee name, salary and manager name
4.Display employee name, manager name and manager salary

5. Display employees whose manager is Steven

6.Display employees whose salary is greater than their manager's salary
7.Display only employees who don't have a manager

8.Display manager name and number of employees working under each manager  ---> self join +group by

9.Display all employees and all departments, including unmatched records ----> full  outer join  ----> use 
10.Display employees who don't belong to any department and departments that don't have any employee.

11.Display every employee with the IT and Sales departments.

task : 1 

1. create database. 
2. create table  
	id  name salary  
    
3. insert ----> 
	5 rows add 
    
4. display only whose  employees whose id is 102 
5. salary >20000   employees name  
6. dispaly  only those employees whose name start with 'A' or 'a'. 

*/ 
create database  dishant;
use dishant;
CREATE TABLE Sale_t (
    sale_id INT,
    sale_date DATE,
    product VARCHAR(50),
    amount DECIMAL(10,2)
);
INSERT INTO Sale_t VALUES
(1, '2024-01-10', 'Laptop', 50000),
(2, '2024-01-15', 'Mouse', 2000),
(3, '2024-02-10', 'Laptop', 60000),
(4, '2024-02-15', 'Mouse', 3000),
(5, '2025-01-10', 'Laptop', 70000),
(6, '2025-01-15', 'Mouse', 4000);

select * from sale_t;
-- 1 .Suppose we want to calculate total sales for each year.

with Sale_cte as 
(
select year(sale_date),sum(amount)
from sale_t 
group by year(sale_date)
) 
select * from sale_cte;

-- 2.
with Sale_cte as 
(
	select year(sale_date) as sale_year ,
    sum(amount) as total_sales
	from sale_t 
	group by year(sale_date)
) 
select sale_year ,total_sales ,lag(total_sales) over(order by sale_year) as previous_yr from sale_cte ;

-- 3.
 with Sale_cte as 
(
	select year(sale_date) as sale_year ,
    sum(amount) as total_sales
	from sale_t 
	group by year(sale_date)
) 
select sale_year ,total_sales ,lag(total_sales) over(order by sale_year) as previous_yr,
ROUND((
            (total_sales - LAG(total_sales) OVER (
                ORDER BY sale_year
            ))
            /
            LAG(total_sales) OVER (
                ORDER BY sale_year
            )
        ) * 100,
        2
    ) AS yoy_growth
FROM Sale_cte;











