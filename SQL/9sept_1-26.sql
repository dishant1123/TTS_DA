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
