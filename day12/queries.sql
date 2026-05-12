create table employees(
	id serial primary key,
	name text not null,
	salary integer
	);

insert into employees(name,salary)
values ('giri',57000),('arun',59000),('prasath',34000),('albert',67000),('john',20000);

update employees
set salary=salary+5700
where name='giri';

delete from employees
where name='albert';

select * from employees;

create table departments(
	id serial primary key ,
	department_name text not null
);

insert into departments(department_name)
values ('hr'),('ai'),('sales'),('production');

select * from departments;


select name,department_name 
from employees as e join departments as d
on e.id=d.id
order by e.name;