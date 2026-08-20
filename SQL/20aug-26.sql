/*
1. select   -----> 
2. *   ----> all row and col 
3. order by ---->  sort  ----> asc to desc  ,  desc to asc 
4. where  ----> condition  
5. case when   ----> if  else ----> manager_id 101   ---->20 %  department_id 90  --->10 % 
6. group by   ----->  group wise  ----> department wise salary   ----> group by  
7. having     ----->  aggre   ---> having   ----> ex : depat wise salary > 10000    group by + having 
8. like  function  ---->  use  ex : 'p'  employees name   display---->  %p ,  p% 
9. IN , between ,isnull ,is not null,and ,or ---->
10. primary key :  not  null ,  unique   
    foreign key :  connect  two  table   ----> primary  ref  to another table 
	superkey  : HW
select  ..... from  .... table_name  ....where .... group by    ..... having ......order by 

JOIN : two  table  merge / join 

type : 

1. INNER JOIN : at least one col  is common  -----> then inner join  possible 
2. LEFT JOIN :  LEFT side all table row col  display  and matching records from another table. 
3. RIGHT JOIN :  RIGHT side all table row col  display  and matching records from another table. 

*/

use scott;

select * from employees;  
select * from  departments;

/*
1.FIRST_NAME, DEPARTMENT_NAME, DEPARTMENT_ID — USING ,ON

2.FIRST_NAME, DEPARTMENT_NAME, DEPARTMENT_ID, BOTH MANAGER_ID — USING ,ON

3.FIRST_NAME, DEPARTMENT_NAME, CITY — USING

4.FIRST_NAME, DEPARTMENT_NAME, CITY, COUNTRY_NAME 

5.DISPLAY DEPARTMENT_NAME , REGION_NAME (ON)

6.Departments in which no employee is hired


7.Employees whose Department_ID is not decided

8.Regions in which no country exists

9.Countries in which no location is fixed

10.Employees who HAVE got promotion ----> use  job_history table 

*/

-- 1.FIRST_NAME, DEPARTMENT_NAME, DEPARTMENT_ID — USING ,ON

select first_name , department_name 
from employees 
inner join departments 
using (department_id);


--  2.FIRST_NAME, DEPARTMENT_NAME, DEPARTMENT_ID, BOTH MANAGER_ID — USING ,ON

select e.first_name ,d.department_name 
from employees e 
inner join departments d 
on e.manager_ID = d.manager_id ;


select e.first_name , d.department_name ,e.manager_id
from employees e 
inner join departments d 
on e.DEPARTMENT_ID =d.DEPARTMENT_ID
inner join departments da 
on e.manager_id = da.MANAGER_ID;

-- 3.FIRST_NAME, DEPARTMENT_NAME, CITY — USING

select * from locations;

select e.first_name , d.department_name,l.city 
from employees e
inner join departments d 
on e.department_id = d.DEPARTMENT_ID
inner join locations l 
on d.LOCATION_ID = l.LOCATION_ID;

-- 4.FIRST_NAME, DEPARTMENT_NAME, CITY, COUNTRY_NAME 
select * from  countries;
