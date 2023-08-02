GRANT ALL PRIVILEGES ON DATABASE  dvdrental TO postgres;

SELECT * FROM category;
SELECT * FROM inventory;
SELECT * FROM customer;
SELECT * FROM rental;
SELECT * FROM film_category;
SELECT * FROM film;
SELECT * FROM payment;
SELECT * FROM language;
SELECT * FROM address;
SELECT * FROM staff;
SELECT * FROM city;
SELECT * FROM country;
SELECT * FROM store;
SELECT * FROM actor;
SELECT * FROM film_actor;

--construye una inserción, modificación y borrado de datos en la tabla customer.
INSERT INTO customer (customer_id, store_id, 'first_name', 'last_name', 'email', address_id, 'activebool', 'create_date', 'last_update', active,);
VALUES (600, 1, 'David', 'Aguilar', 'aguilardavid@hotmail.com', 606, 'true', '2006-02-14', '2013-05-26 14:49:45.738', 1);
UPDATE customer SET emmail = 'aguilardavid@hotmail.com' WHERE customer_id = 62;
DELETE FROM customer WHERE customer_id = 83;

--construye una inserción, modificación y borrado de datos en la tabla staff.
INSERT INTO staff (staff_id, 'first_name', 'last_name', 'address_id','email', store_id, 'active', 'username', 'password', 'last_update', 'picture',);
VALUES (3, 'David', 'Aguilar', 5, 'aguilardavid@hotmail.com', 3, 'true', 'David', '8cb2237d0679ca88db6464eac60da96345513964', '2006-05-16 16:13:11.79328',[null]);
UPDATE staff SET first_name = Tony WHERE staff_id = 2;
DELETE FROM staff WHERE staff_id = 1;

--construye una inserción, modificación y borrado de datos en la tabla actor.

UPDATE actor SET first_name = Tony WHERE actor_id = 173;
DELETE FROM actor WHERE actor_id = 194;
INSERT INTO actor (actor_id, 'first_name', 'last_name', 'last_update',);
VALUES (194, 'David', 'Aguilar', 2013-05-26 14:47:57.62,);

--Listar todas las “rental” con los datos del “customer” dado un año y mes.
SELECT r.*, c.* FROM rental as r
JOIN customer as c
ON r.customer_id = c.customer_id
WHERE r.rental_date BETWEEN '2005-05-01' AND '2005-05-31';

SELECT CAST (payment_date as DATE) FROM payment;
SELECT payment_date::DATE FROM payment;
SELECT payment_date::TIME FROM payment;

SELECT * FROM film
	WHERE release_year = 2006 AND rental_rate > 4;
	
SELECT tl.TABLE_NAME AS tabla_nombre,
	t1.COLUMN_NAME AS columna_nombre,
	t1.COLUMN_DEFAULT AS columna_defecto,
