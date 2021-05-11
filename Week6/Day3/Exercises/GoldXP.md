-- Ex1

-- select * from rental
-- where return_date is null;
-- 1)
-- select film.title, film.film_id, inventory.inventory_id, rental.rental_id
-- from inventory
-- inner join film
-- on film.film_id = inventory.film_id
-- inner join rental
-- on rental.inventory_id = inventory.inventory_id
-- where rental.return_date is null;

-- 2)
-- select customer.first_name, customer.last_name, count(customer.customer_id)
-- from rental
-- inner join customer 
-- on rental.customer_id = customer.customer_id
-- where rental.return_date is null
-- group by customer.first_name, customer.last_name
-- order by count desc;


-- 3)
-- create view action_movies2 as
-- 	select film.film_id
-- 	from film_category 
-- 	inner join category
-- 	on category.category_id = film_category.category_id
-- 	inner join film
-- 	on film.film_id = film_category.film_id
-- 	where category.name = 'Action';
	
-- select * from action_movies2

-- select film.film_id, film.title, actor.first_name, actor.last_name
-- from film_actor
-- inner join film
-- on film.film_id = film_actor.film_id
-- inner join actor
-- on actor.actor_id = film_actor.actor_id
-- where actor.first_name = 'Joe'
-- and actor.last_name = 'Swank'
-- and film.film_id in (select film_id from action_movies2)



-- Ex2
-- Ex2
-- 1)
-- create view locations2 as 
-- select store.store_id,city.city, country.country
-- from store 
-- inner join address 
-- on store.address_id = address.address_id
-- inner join city 
-- on address.city_id = city.city_id
-- inner join country
-- on city.country_id = country.country_id

-- 2 + 3)
-- select sum(film.length), locations2.city, locations2. country
-- from locations2 
-- inner join customer
-- on locations2.store_id = customer.store_id
-- inner join rental
-- on customer.customer_id = rental.customer_id
-- inner join inventory
-- on inventory.inventory_id = rental.inventory_id
-- inner join film
-- on film.film_id = inventory.film_id
-- where rental.return_date is not null
-- group by locations2.city, locations2.country

-- select * from locations2

-- 4)
-- select customer.first_name, customer.last_name, city.city
-- from store
-- inner join customer
-- on store.store_id = customer.store_id
-- inner join address
-- on customer.address_id = address.address_id
-- inner join city
-- on city.city_id = address.city_id
-- where city.city in (select city from locations2)


-- select * from locations2

-- 5)
-- select customer.first_name, customer.last_name, country.country
-- from store
-- inner join customer
-- on store.store_id = customer.store_id
-- inner join address
-- on customer.address_id = address.address_id
-- inner join city
-- on city.city_id = address.city_id
-- inner join country
-- on country.country_id = city.country_id
-- where country.country in (select country from locations2)