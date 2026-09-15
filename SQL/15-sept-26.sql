/*
CRUD : operation : 

-----> create  
-----> read 
-----> update
-----> delete

*/

create database if not exists DA_students;

use da_students;

create  table if not exists students_info (
	id int auto_increment primary key,
    name varchar(30),
    salary int8,
    age int2
);

drop table student_info;   -- delete  

-- insert table  : 

insert into students_info 
values 
(1,"raju",45000,40),
(2,"jay",55000,25),
(3,"bhavesh",42000,24),
(4,"vansh",50000,28),
(5,"sujal",20000,21);

select * from students_info;

insert into students_info 
values
(6,"roshni",230000,23); 

-- update ------>roshni salary  update  -----> 56000 

update students_info  
set salary =56000 
where id=6; 

select name,salary from students_info;

-- update ------>roshni salary  update  -----> 56000  ,age -21  ,name --> varun

update students_info  
set salary =96000,
	name ="varun",
    age =21
where id=6;

select name,salary from students_info;

-- delete  id =2 

delete from students_info 
where id =2;

select id,name,salary from students_info;
 
 
-- commit- ---> save , rollback --> undo 

/*
1.create  new  database 
2. table id name  salary  age city  
3. update 
4. print only  those name  which name  start  with 's'; 
5. print only  those name  which  second letter start with 'a';
6. salary  > 40000 print  name  
7. city  wise salary 
8. city wise  salary and  print only those name  who's has  avg salary more than 9000. 
9. sort salary by desc to asc and  give the  rank  like 1,2,3,..... using window  function  . 
10. delete the  id wise ,col wise ,name wise 

/* 






 

