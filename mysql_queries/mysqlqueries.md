SYNTAX
create database database_name;
use database_name; -- to switch to a database
show databases; -- to list databases

create table table_name(
    column_name data_type constraint,
    column_name data_type constraint,
);

desc table_name; -- to describe table
DISPLAY
select * from table_name
INSERT
insert into table_name(col1,col2) values(val1,val2);
UPDATE
update table_name set col1=val1,col2=val2 where condition