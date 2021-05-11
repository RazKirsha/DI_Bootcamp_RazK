-- create table movies(
-- 	movie_id serial,
-- 	movie_title varchar (50) not null,
-- 	movie_story text,
-- 	actor_playing_id integer,
-- 	primary key (movie_id),
-- 	foreign key (actor_playing_id) references actors(actor_id)
-- );

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
--     ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id;

-- create table producers(
-- 	producer_id serial,
-- 	movie_id int not null,
-- 	producers_name varchar(50),
-- 	primary key (producer_id),
-- 	foreign key (movie_id) references movies(movie_id)
-- );

-- insert into producers (movie_id, producers_name)
-- values
-- ((select movie_id from movies where movie_title = 'Oceans Eleven'),'Steffen Spielberg')

select movies.movie_title, producers.producers_name
from movies
inner join producers
on producers.movie_id = movies.movie_id;
