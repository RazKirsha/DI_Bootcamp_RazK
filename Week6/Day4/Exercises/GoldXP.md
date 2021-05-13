-- Ex1
-- 1)
-- update employees
-- set 
-- 	email = 'unavailable'
-- where
-- 	department_id = 110
-- returning *;

-- select * from employees

-- 2)
-- update employees
-- set 
-- 	email = 'available'
-- where
-- department_id = (select department_id id from
-- (select distinct employees.department_id,  departments.department_name
-- from employees
-- inner join departments
-- on departments.department_id = employees.department_id
-- where departments.department_name = 'Accounting') as accounting)

-- select * from departments

-- select department_id id from
-- (select distinct employees.department_id,  departments.department_name
-- from employees
-- inner join departments
-- on departments.department_id = employees.department_id
-- where departments.department_name = 'Accounting') as accounting

-- select * from employees 
-- where
-- department_id = (select department_id id from
-- (select distinct employees.department_id,  departments.department_name
-- from employees
-- inner join departments
-- on departments.department_id = employees.department_id
-- where departments.department_name = 'Accounting') as accounting)


-- 3)
-- update employees 
-- set salary = 8000
-- where 
-- employee_id = 105 
-- and salary < 5000
-- returning *;

-- Ex2
-- 1)
-- select count(*) from employees

-- 2)
-- select jobs.job_title, count(jobs.job_title)
-- from jobs
-- left outer join employees
-- on jobs.job_id = employees.job_id
-- group by jobs.job_title

-- 3)
-- select max(salary)-min(salary) from employees

-- 4) 
-- select manager_id, salary
-- from employees
-- order by salary asc
-- limit 1;

-- 5)
-- select round(avg(employees.salary),2) , jobs.job_title
-- from employees 
-- inner join jobs
-- on employees.job_id = jobs.job_id
-- where jobs.job_title != 'programmer'
-- group by jobs.job_title

-- 6) 
-- select * 
-- from 
-- (select count(employees.job_id), round(avg(employees.salary),2) , jobs.job_title
-- from employees 
-- inner join jobs
-- on employees.job_id = jobs.job_id
-- group by jobs.job_title) as jobs_stats
-- where count > 10

-- Ex3
-- 1)
-- alter table locations
-- rename column state_province to state

-- select * from locations

-- 2)
-- alter table locations
-- add primary key(location_id)

-- Ex4
-- 1)
-- create table new_countries (
-- 	country_id serial primary key,
-- 	country_name text not null,
-- 	check (country_name = 'Italy'
-- 		   or country_name = 'India'
-- 		   or country_name = 'China')
-- )

-- insert into new_countries(country_name)
-- values
-- ('Brazil')

-- 2)
-- select *
-- into new_countries2
-- from new_countries
-- where 1 = 2

-- select * from new_countries2

-- 3)
-- create table new_jobs (
-- 	job_id serial primary key,
-- 	job_title text default 'blank',
-- 	min_salary smallint default 8000,
-- 	max_salary smallint default null,
-- 	check (
-- 		max_salary < 25000
-- 	)
-- )

-- 4)
-- create table new_employees(
-- 	employee_id serial unique primary key,
-- 	first_name varchar(50),
-- 	last_name varchar(100),
-- 	email varchar(100),
-- 	phone_number varchar(100),
-- 	hire_date date,
-- 	job_id int,
-- 	salary int,
-- 	foreign key (job_id) references new_jobs(job_id)
-- )

-- 5)
-- create table new_job_history (
-- 	employee_id int,
-- 	start_date date,
-- 	end_date date,
-- 	job_id int,
-- 	foreign key (employee_id) references new_employees(employee_id) on delete cascade,
-- 	foreign key (job_id) references new_jobs(job_id) on delete cascade
-- )

-- Ex5
-- 1)
-- insert into new_countries(country_name)
-- values
-- ('China');

-- select * from new_countries;

-- 2)
-- insert into new_countries(country_name)
-- values
-- ('Italy'),
-- ('India');

-- select * from new_countries;
-- select * from new_countries2;

-- 3) 
-- insert into new_countries2(country_name)
-- select country_name from new_countries;