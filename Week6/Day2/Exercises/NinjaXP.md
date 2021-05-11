-- select first_name, last_name
-- from customers
-- order by first_name desc
-- limit 2;

-- select * from purchases
-- delete from purchases 
-- where customer_id = 3
-- returning *;

-- select * from customers

-- select * from purchases
-- select customers.first_name, customers.last_name, items.product
-- from purchases
-- inner join customers
-- on customers.customer_id = purchases.customer_id
-- inner join items
-- on items.item_id = purchases.item_id;