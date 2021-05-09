-- SELECT * FROM students
-- SELECT first_name, last_name from students
-- WHERE student_id = 2;
-- WHERE last_name = 'Benichou' AND first_name = 'Marc';
-- WHERE first_name LIKE '%a%';
-- WHERE first_name LIKE 'a%';
-- WHERE first_name LIKE '%a';
-- WHERE LEFT(RIGHT(first_name,2),1) = 'a';
-- WHERE student_id = 1 or student_id = 3;
SELECT * FROM students
WHERE birth_date >= '01/01/2000'