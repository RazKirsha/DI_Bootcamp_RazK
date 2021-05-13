-- Ex1
-- 1)
-- select first_name as "First Name", last_name as "Last Name" from employees

-- 2)
-- select distinct department_id from employees
-- order by department_id asc;

-- 3)
-- select * from employees 
-- order by first_name desc;

-- 4) 
-- select first_name, last_name, salary, 0.15*salary as "PF" 
-- from employees;

-- 5)
-- select employee_id, first_name,last_name, salary from employees
-- order by salary asc;

-- 6)
-- select sum(salary) from employees;

-- 7)
-- select max(salary), min(salary) from employees;

-- 8)
-- select avg(salary) from employees

-- 9)
-- select count(employee_id) from employees

-- 10)
-- select upper(first_name) from employees

-- 11)
-- select substring(first_name,1,3) from employees

-- 12)
-- select concat(first_name,' ', last_name) as "Full Name" from employees

-- 13)
-- select first_name, last_name, length(concat(first_name,' ', last_name)) as "Full Name Length"  from employees

-- 14)
-- select count(first_name) from employees where first_name like '%[^0-9]%'

-- 15)
-- select * from employees
-- order by employee_id asc
-- limit 10;


-- Ex2
-- 1)
-- select first_name, last_name, salary 
-- from employees
-- where salary>10000 and salary<15000;

-- 2)
-- select first_name,last_name,hire_date as hire
-- from employees
-- where extract(year from hire_date)= 1987;

-- 3)
-- select * from employees
-- where first_name like '%e%' 
-- and first_name like '%c%' ;

-- 4)
-- select employees.first_name, employees.last_name, jobs.job_title, salary
-- from employees
-- inner join jobs
-- on jobs.job_id = employees.job_id
-- where jobs.job_title != 'Programmer '
-- and jobs.job_title != 'Shipping Clerck'
-- and employees.salary != 4500
-- and employees.salary != 10000
-- and employees.salary != 15000;

-- 5)
-- select last_name from employees 
-- where length(last_name) = 6;

-- 6)
-- select last_name from employees
-- where substring(last_name,3,1) = 'e';

-- 7)
-- select jobs.job_title, count(jobs.job_title)
-- from jobs
-- left outer join employees
-- on jobs.job_id = employees.job_id
-- group by jobs.job_title

-- 8)
select * from employees
where upper(last_name) = 'JONES'
or upper(last_name) = 'BLAKE'
or upper(last_name) = 'SCOTT'
or upper(last_name) = 'KING'
or upper(last_name) = 'FORD'

