-- everything on exercise 1
-- from 1 - 3.2 got deleted!
-- this is from 3.3~~~

-- from purchases
-- inner join items
-- on purchases.item_id = items.item_id
-- where purchases.customer_id = 4;

-- select purchases.customer_id, items.product
-- from purchases
-- inner join items
-- on purchases.item_id = items.item_id
-- where product = 'Small Desk' or product = 'Large Desk';

-- insert into items (product, price)
-- values('Hard drive', 150);
-- select * from items;
-- select * from purchases;
-- insert into purchases (customer_id,item_id)
-- values
-- ((select customer_id from customers where first_name = 'Scott'),
--  (select item_id from items where product = 'Hard drive'));
-- select * from purchases;

select customers.first_name, customers.last_name, items.product
from purchases
inner join customers
on customers.customer_id = purchases.customer_id
inner join items
on items.item_id = purchases.item_id;

-- Ex2
-- 2.1)
-- select * from customer

-- 2.2)
-- select first_name, last_name from customer as full_name

--2.3)
-- select distinct create_date from customer;

-- 2.4)
-- select * from customer
-- order by first_name desc;

-- 2.5)
-- select film_id, title, description, release_year, rental_rate
-- from film
-- order by rental_rate desc;

-- 2.6)
-- select address, phone 
-- from address 
-- where district = 'Texas';

-- 2.7)
-- select * from film where film_id = 15 or film_id = 150;

-- 2.8)
-- select film_id, title, description, length, rental_rate
-- from film
-- where title = 'Cider Desire';

-- 2.9)
-- select film_id, title, description, length, rental_rate
-- from film
-- where title like 'Ci%';

-- 2.10)
-- select * from payment
-- order by amount asc
-- limit 10;

-- 2.11)
-- select * from payment
-- order by amount asc
-- offset 10 limit 10;

-- 2.12)
-- select payment.customer_id, customer.first_name, customer.last_name, payment.payment_date
-- from payment
-- inner join customer 
-- on payment.customer_id = customer.customer_id
-- order by payment.customer_id asc;

--2.13)
-- select *
-- from inventory
-- where inventory_id not in (select film_id from inventory);

--2.14)
-- select city.city, country.country
-- from city
-- inner join country
-- on city.country_id = country.country_id
-- order by country.country asc;

--2.15)
select payment.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date
from payment
inner join customer
on payment.customer_id = customer.customer_id
order by payment.staff_id asc;
