-- create table tstudent(tsis int, sname varchar(25),fname varchar(25))
-- insert into tstudent values(1,'John','Ron')
-- insert into tstudent(sname,fname,tsis) values('Maria','Sam',2);
-- insert into tstudent(sname,fname,tsis) values('Maria1','Sam1',3);
-- insert into tstudent(sname,fname,tsis) values('Maria2','Sam2',4);
-- insert into tstudent(sname,fname,tsis) values('Maria3','Sam3',5);
-- insert into tstudent(tsis,sname,fname) values(6,'a','a1'),(7,'b','b1'),(8,'c','c1')

-- select * from tstudent
-- select sname,fname from tstudent
-- select sname as Name,fname as Fathers_name from tstudent
-- select * from tstudent where tsis =6
-- select count(*) from tstudent
-- select * from tstudent limit 3
-- select distinct tsis from tstudent
-- select distinct tsis,sname,fname from tstudent
-- select distinct tsis,sname,fname from tstudent order by tsis
-- select distinct tsis,sname,fname from tstudent order by tsis desc
-- select * from tstudent offset 5
select * from tstudent offset 5 limit 3