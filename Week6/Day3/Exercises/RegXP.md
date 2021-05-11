--Ex1
-- 1)
-- select * from language;

--2)
--2.1)
-- select film.title, film.description, language.name
-- from film
-- left outer join language
-- on film.language_id = language.language_id

--2.2)
-- select film.title, film.description, language.name
-- from film
-- right outer join language
-- on film.language_id = language.language_id
-- -- where title is null

--3)
-- create table new_film (
-- 	id serial primary key,
-- 	name text
-- )

-- select * from new_film
-- select title from film

-- insert into new_film (name)
-- values
-- ('Watchmen'),
-- ('The Flash'),
-- ('Avengers'),
-- ('Batman');

-- select * from new_film

--4)
-- create table customer_review (
-- 	review_id serial primary key,
-- 	film_id int,
-- 	language_id int,
-- 	title varchar(100),
-- 	score smallint,
-- 	review_text text,
-- 	last_update date,
-- 	foreign key(film_id) references new_film(id) on delete cascade, 
-- 	foreign key (language_id) references language(language_id)
-- )

-- select * from customer_review
-- select * from new_film

-- 5)
-- select * from language
-- insert into customer_review
-- (film_id, language_id, title, score, review_text, last_update)
-- values
-- (1,1,'Good Movie', 10, 'This was a great movie','11/05/2021'),
-- (3,5,'Bad Movie', 10, 'This was not a good movie at all','05/10/2020')
-- select * from customer_review
-- select 
-- new_film.name, language.name, customer_review.score, customer_review.review_text
-- from customer_review
-- inner join new_film 
-- on customer_review.film_id = new_film.id
-- inner join language
-- on customer_review.language_id = language.language_id

-- 6)
-- delete from customer_review where film_id = 3
-- select 
-- new_film.name, language.name, customer_review.score, customer_review.review_text
-- from customer_review
-- inner join new_film 
-- on customer_review.film_id = new_film.id
-- inner join language
-- on customer_review.language_id = language.language_id


-- Ex2
-- 1)
-- update film 
-- set language_id = 6 
-- where title like 'B%'
-- returning *;

-- select * from film
-- order by title asc;

-- 2)
-- select * from customer

-- 3)
-- drop table customer_review

-- 4)
-- select count(*) from rental
-- where return_date is null;

-- 5)
-- select rental_id from rental
-- where return_date is null
-- order by rental_id asc;

-- select rental.rental_id, payment.amount as price
-- from payment
-- inner join rental 
-- on payment.rental_id = rental.rental_id
-- where rental.return_date is null
-- order by price desc
-- limit 30;

-- 6)
-- 6.1)
-- select film.title, film.description, actor.first_name, actor.last_name 
-- from film_actor
-- inner join actor
-- on actor.actor_id = film_actor.actor_id
-- inner join film
-- on film.film_id = film_actor.film_id
-- where first_name = 'Penelope'
-- and last_name = 'Monroe'
-- and description like '%Sumo%';

-- 6.2)
-- select film.title, film.length, film.rating, category.name
-- from film_category
-- inner join film
-- on film.film_id = film_category.film_id
-- inner join category
-- on category.category_id = film_category.category_id
-- where length < 60
-- and rating = 'R'
-- and name = 'Documentary'

-- 6.3)
-- MY WAY
-- select distinct rental.inventory_id
-- from rental
-- inner join customer
-- on customer.customer_id = rental.customer_id
-- inner join payment
-- on payment.customer_id = rental.customer_id
-- where '2005-08-01' >= return_date
-- and return_date >= '2005-07-28'
-- and amount > 4.00
-- and first_name = 'Matthew'
-- and last_name = 'Mahan'

-- select distinct film.title
-- from inventory 
-- inner join rental
-- on rental.inventory_id = inventory.inventory_id
-- inner join film
-- on film.film_id = inventory.film_id
-- where inventory.inventory_id in (select inventory_id  -- from possible)
 
OR
-- CHAIMS WAY
-- select film.title, customer.first_name, customer.last_name, payment.payment_id, payment.amount, rental.return_date
-- from rental
-- inner join customer
-- on rental.customer_id = customer.customer_id
-- inner join payment
-- on rental.rental_id = payment.rental_id
-- inner join inventory
-- on rental.inventory_id = inventory.inventory_id
-- inner join film
-- on inventory.film_id = film.film_id
-- where customer.first_name = 'Matthew'
-- and customer.last_name = 'Mahan'
-- and rental.return_date < '2005-08-01'
-- and rental.return_date > '2005-07-28'
-- and payment.amount > 4

-- 6.4)
-- select film.title, film.description, customer.first_name, customer.last_name, payment.payment_id, payment.amount, rental.return_date
-- from rental
-- inner join customer
-- on rental.customer_id = customer.customer_id
-- inner join payment
-- on rental.rental_id = payment.rental_id
-- inner join inventory
-- on rental.inventory_id = inventory.inventory_id
-- inner join film
-- on inventory.film_id = film.film_id
-- where customer.first_name = 'Matthew'
-- and customer.last_name = 'Mahan'
-- and (title like '%Boat%' or description like '%Boat%')
-- order by payment.amount desc
-- limit 1;