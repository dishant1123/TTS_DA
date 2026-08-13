/*
output  :1

FIRST_NAME          SALARY NVL(COMMISSION_PCT,0) COMM_AMOUNT TOTAL_PAYMENT                                                                                                                              
--------------- ---------- --------------------- ----------- -------------                                                                                                                              
Steven               24000                     0           0         24000                                                                                                                              
Neena                17000                     0           0         17000                                                                                                                              
Lex                  17000                     0           0         17000                                                                                                                              
Alexander             9000                     0           0          9000                                                                                                                              
Bruce                 6000                     0           0          6000                                                                                                                              
Diana                 4200                     0           0          4200                                                                                                                              
Kevin                 5800                     0           0          5800                                                                                                                              
Trenna                3500                     0           0          3500                                                                                                                              
Curtis                3100                     0           0          3100                                                                                                                              
Randall               2600                     0           0          2600                                                                                                                              
Peter                 2500                     0           0          2500                                                                                                                              
Eleni                10500                    .2        2100         12600                                                                                                                              
Ellen                11000                    .3        3300         14300                                                                                                                              
Jonathon              8600                    .3        2580         11180                                                                                                                              
Kimerely              7000                   .15        1050          8050  

===========================================================================


1. increment the salary 20% 
2. INCREMENT IS BASED ON DEPARTMENT_ID : 20 +2000 , 50 +1500 , 80 +1000 , REMAINING +500 ---->case when 

3. MANAGER_ID : 100 40% , 124 +1500 , 149 20% , REMAINING 12.5%

4. BASED SALARY RANGE : 0-6000 40% , 6001-9000 30% , 9001-13000 20% , REMAINING 10%
-- hint  between 	
5. HW :JOB_ID : IT_PROG MK_MAN +2000 , SA_REP MK_REP AD_ASST +1500 , ST_CLERK AD_VP +1000 , REMAINING +500

6. department wise min max avg salary . ----> group by

7.COUNT THOSE WHO WORKS IN DEPARTMENT 50

8. department wise avg salary and display  salary >7500 ----> group by +having

9.DISPLAY JOB WISE TOTAL SALARY, DISPLAY ONLY THOSE ROW WHICH HAS HIGHEST SALARY LOWER THAN 10000 ---> group by +having

10 .DISPLAY JOB WISE TOTAL SALARY, DISPLAY ROWS OF IT_PROG ST_CLERK AD_VP ----> group by +having +IN
-- id  name  salary  
insert into emp_infor values (1,"fh",90000),
							(2,'aekeo', 8000),
							(3,'efew',7000);	
		
*/

use scott;
select * from employees;
-- 7. 
select count(*) from 
employees 
where department_id=50;

-- 1.  salary 20% incerement :

select first_name ,salary , salary*1.20 inc_salary
from 
employees; 

-- 2. commission pct 

select first_name ,salary , 
ifnull(commission_pct,0),
salary * ifnull(COMMISSION_PCT,0) comm_amt ,
salary + salary * ifnull(commission_pct,0) total_payment
from employees;

-- 3. INCREMENT IS BASED ON DEPARTMENT_ID : 20 +2000 , 50 +1500 , 80 +1000 , REMAINING +500 ---->case when 

select first_name, salary ,department_id ,
case DEPARTMENT_ID when 20 then salary +2000
				   when 50 then salary +1500
				   when 80 then salary+1000
                   else salary +500
				END as inc_depart_salary
from employees;

-- MANAGER_ID : 100 40% , 124 +1500 , 149 20% , REMAINING 12.5%

select first_name,manager_id,salary , 
case manager_id when 100  then salary *1.4
				when 124 then salary +1500
				when 149 then salary *1.25
                else salary*1.125
		END as inc_salary 
from employees;


-- 6.department wise min max avg salary . ----> group by
select department_id,min(salary) as min_salary, max(salary) as max_salary , avg(salary) as avg_salary  
from employees
group by department_id;




