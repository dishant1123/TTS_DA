/* 
window function  : 

1. OVER():
	OVER() tells SQL:
	"Perform this calculation as a window function."

2.PARTITION BY:
	PARTITION BY divides the data into groups, but does not remove individual rows.


3. ROW_NUMBER()
	ROW_NUMBER() gives a unique number to every row.


4. ROW_NUMBER() with PARTITION BY

5.RANK()
	RANK() gives the same rank when values are tied.

6.DENSE_RANK()

	DENSE_RANK() also gives the same rank for tied values.

*/ 
/*
1. OVER():
	OVER() tells SQL:
	"Perform this calculation as a window function."
*/ 
use scott; 
select * from employees;

select  first_name,department_id,salary,
avg(salary)
over() as com_avg_salary
from employees;

-- select  first_name avg salary from employees group by department_id

/* 
id   first_name  salary  department_id  avg_salary   rank 
1    ram         11000      12            8733       2  
2    sita        11000     12            8733        2
3    ravan       15000     90            8733        1
4    laxman      3000      11            8733        4
5    bhudev      1000      12            8733        5

*/ 
/* 
2.PARTITION BY:
	PARTITION BY divides the data into groups, but does not remove individual rows.
*/ 
select  first_name,department_id,salary,
avg(salary)
over(partition by department_id ) as departmetwise_avg_salary
from employees;

/*
3. ROW_NUMBER()
	ROW_NUMBER() gives a unique number to every row.
*/ 

select  first_name , 
salary , 
ROW_NUMBER()
over() as num_emp
from employees; 

-- 4. ROW_NUMBER() with PARTITION BY-- 
select  first_name,department_id,salary,
ROW_NUMBER()
over(partition by department_id ) as departmetwise_salary
from employees;

-- 5 . 5.RANK() ---> RANK() gives the same rank when values are tied.

select first_name ,salary,
rank() 
over( order by salary desc) as desc_salary 
from employees limit 4; 

-- 6.DENSE_RANK() :	DENSE_RANK() also gives the same rank for tied values.

select first_name ,salary,
dense_rank()
over( order by salary desc) as desc_salary 
from employees; 

use dishant ;
CREATE TABLE sales (
    sale_id INT,
    salesperson VARCHAR(50),
    region VARCHAR(30),
    product VARCHAR(50),
    sale_amount INT,
    sale_date DATE
);

INSERT INTO sales VALUES
(1, 'Amit',   'North', 'Laptop',   80000, '2025-01-10'),
(2, 'Priya',  'North', 'Mobile',   50000, '2025-01-12'),
(3, 'Rahul',  'North', 'Laptop',   80000, '2025-02-05'),
(4, 'Neha',   'North', 'Tablet',   40000, '2025-02-15'),

(5, 'Karan',  'South', 'Laptop',   90000, '2025-01-08'),
(6, 'Sneha',  'South', 'Mobile',   60000, '2025-01-20'),
(7, 'Vikas',  'South', 'Laptop',   90000, '2025-02-10'),
(8, 'Pooja',  'South', 'Tablet',   45000, '2025-02-18'),

(9,  'Ravi',   'West', 'Laptop',   70000, '2025-01-05'),
(10, 'Anjali', 'West', 'Mobile',   55000, '2025-01-15'),
(11, 'Mehul',  'West', 'Laptop',   70000, '2025-02-01'),
(12, 'Komal',  'West', 'Tablet',   35000, '2025-02-20');

select * from sales;

-- 13 : 
select  * , 
rank() 
over (order by sale_amount desc ) as sale_amt_desc 
from  sales; 

-- 14 . 
select  salesperson ,region,sale_amount ,
rank() 
over (partition by region
	order by sale_amount desc
	  ) as sale_rank 
from  sales;  

-- 15 : 
with  sale_cte as  (
select  salesperson ,region,sale_amount ,
rank() 
over (partition by region
	order by sale_amount desc
	  ) as sale_rank 
from  sales 
)
select salesperson , region,sale_amount 
from  
sale_cte 
where sale_rank =1;

-- 16 . 
with  sale_cte as  (
select  salesperson ,region,sale_amount ,
rank() 
over (partition by region
	order by sale_amount desc
	  ) as sale_rank 
from  sales 
)
select salesperson , region,sale_amount 
from  
sale_cte 
where sale_rank <=2;






