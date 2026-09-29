/*
commit  : permenent  save  
rollback  : undo 

*/
SET autocommit = 0;

create  database demo_commit;  
use demo_commit;

create table  d_rollback(
id int, 
name varchar(20),
salary int
) ; 

insert into d_rollback values 
( 101,"ram",10000),
( 102,"sita",1000),
( 103,"ravan",90000);

update d_rollback 
set salary =400000 
where id =102; 

update d_rollback 
set salary =4000000 
where id =101; 

rollback; 

select * from  d_rollback;
/* ======================================================== */ 
 -- String  function  :
 
 /*
 1. lower 
2. upper
3. substr(extract part of the string )
4. left 
5. right 
6. replace 
7. trim 

 */

CREATE DATABASE string_demo;
USE string_demo;

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    product_code VARCHAR(50),
    category VARCHAR(50)
);

INSERT INTO products
VALUES
(1, 'Laptop', ' lap-101 ', 'Electronics'),
(2, 'Mouse', 'MOU-202', 'electronics'),
(3, 'Keyboard', ' key-303 ', 'ELECTRONICS'),
(4, 'Monitor', 'MON-404', 'Electronics'),
(5, 'Printer', ' pri-505 ', 'Office');

select * from products;

select product_id , 
lower(product_name) 
from products;

select product_id , 
upper(category) 
from products; 

select product_id , 
trim(product_code) 
from products; 

select product_id , 
replace(product_code,'-','') 
from products; 

select product_id , 
substr(product_code,1,3) as clean 
from products; 

select product_id , 
left(product_code,4) as clean 
from products; 

select product_id , 
right(product_code,8) as clean 
from products; 



