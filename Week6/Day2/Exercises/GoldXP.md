--Ex1

-- select count(rating)
-- from film 

-- select *
-- from film
-- where rating = 'G' or rating = 'PG-13' 
-- and length < 120
-- and rental_rate <= 3.00
-- order by title asc;

-- update customer 
-- set first_name = 'Raz',
-- 	last_name = 'Kirsha',
-- 	email = 'RRR@gmail.com'
-- where customer_id = 3;

-- select * from customer
-- order by customer_id asc;

-- update customer 
-- set 
-- 	address_id = 8
-- where 
-- 	first_name = 'Raz'
-- 	and
-- 	last_name = 'Kirsha';

-- select * from customer
-- order by customer_id asc;


-- Ex2
-- update students 
-- set 
-- 	birth_date = '02/11/1998'
-- where 
-- 	last_name = 'Benichou';

-- select * from students;

-- delete from students 
-- where 
-- 	first_name = 'Lea' and last_name = 'Benichou'
-- returning *;

-- select count(*) 
-- from students;

-- select * from students;

-- select count(*)
-- from students
-- where birth_date > '01/01/2000';

-- select * from students;

-- alter table students add column math_grade int;

-- select * from students;

-- update students
-- set math_grade = 80
-- where student_id = 1;

-- update students
-- set math_grade = 90
-- where student_id = 2 or student_id = 4;

-- update students
-- set math_grade = 40
-- where student_id = 6;

-- select count (*)
-- from students 
-- where math_grade > 83;

-- insert into students (first_name, last_name, birth_date, math_grade)
-- values
-- 	('Omer', 'Simpson', '03/10/1980',70)

select * from students;
