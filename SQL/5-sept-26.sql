/*   
CTE : common table  expression : 
1 .Suppose we want to calculate total sales for each year.
2.Suppose we only want years where sales are greater than ₹100,000.

3. CTE for YoY Growth  : YoY : year over year  ------> use  LAG() function  in SQL 
	(current year - previous year) 
 		------------------	* 100	 
                   previous yr

4.Display those years where total sales are greater than 100000.

5. suppose we have another table called 

customers : 
Display customers whose total sales are greater than 50000.

| customer_id | customer_name |
| ----------: | ------------- |
|         101 | Rahul         |
|         102 | Priya         |
|         103 | Amit          |

| sale_id | customer_id | sale_date  | amount |
| ------: | ----------: | ---------- | -----: |
|       1 |         101 | 2024-01-10 |  50000 |
|       2 |         102 | 2024-01-15 |   2000 |
|       3 |         101 | 2024-02-10 |  60000 |
|       4 |         103 | 2024-02-15 |   3000 |
|       5 |         102 | 2025-01-10 |  70000 |
|       6 |         103 | 2025-01-15 |   4000 |
6.CTE + JOIN + HAVING
Display each customer and their total sales, but only show customers whose total sales are greater than 50000.

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

-- 1. Suppose we want to calculate total sales for each year. 
with sale_cte as 
(
	select year(sale_date) as year_wise ,
	sum(amount) as total_sales 
	from  sale_t 
	group by year(sale_date) 
)
select * from sale_cte;

-- 2. Suppose we only want years where sales are greater than ₹100,000.
with sale_cte as 
(
	select year(sale_date) as year_wise ,
	sum(amount) as total_sales 
	from  sale_t 
	group by year(sale_date) 
)
select * from sale_cte 
where total_sales > 100000;

/*
year     total_sales    previous_sale 
2023      90000            na
2024      115000           90000 
2025      74000           115000 

over () -------> window function  -----> rows agg use 
lag()   ------> previous yr 

-- 3. previous yr sale:


*/
-- 3. previous yr sale 
with sale_cte as 
(
	select year(sale_date) as year_wise ,
	sum(amount) as total_sales 
	from  sale_t 
	group by year(sale_date) 
),
sale_comparison as 
(
	select year_wise , 
    total_sales, 
    lag(total_sales) over(order by year_wise ) as py_sales
    from sale_cte
)
select year_wise , 
    total_sales, 
    py_sales ,
    round(
    ((total_sales -py_sales) /py_sales)*100 ,2
    ) as yoy_growth
from sale_comparison;
/*
((total sales - py sales )  / pysales ) *100 ----> 74 - 115000 / 115000  ====> -34 % 
*/
-- hw : add one year  and give total sales  and calculate the growth rate. 

