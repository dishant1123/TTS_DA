/*
day  month year  -----> 

id   name   joining_date   -----> date
1    ram     16/06/2009    =day() , =year(), =month()
2    sita    1/1/2004
3    ravan   1/3/2001

*/

use da_students;

create table orders(
	id int ,
    name varchar(30), 
    joining_date date

);

insert into orders values 
(1,"ram",'2006-06-16'),
(2,"vansh",'2026-10-12'),
(3,"piyush",'2029-06-20'),
(4,"varun",'2003-03-20');

select * from orders; 

-- days  , month  , year 

select name ,joining_date, 
day(joining_date) as days ,
month(joining_date) as month , 
year(joining_date) as year  
from 
orders; 





