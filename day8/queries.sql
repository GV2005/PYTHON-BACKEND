CREATE TABLE employees(
	id  INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	department TEXT,
	salary INTEGER,
	city TEXT);

INSERT INTO employees (name,department,salary,city)
VALUES ("giri","ai&ds",45000,"chennai"),
("arun","ai&ds",45000,"chennai"),
("prasath","ai&ds",40000,"chennai"),
("harish","it",49000,"cbe"),
("gandhi","mech",35000,"trichy"),
("albert","cse",27000,"bangalore");

SELECT * FROM employees;

SELECT * FROM employees WHERE city="chennai";

SELECT * FROM employees WHERE city="chennai" AND salary>=40000;

SELECT * FROM employees WHERE city="chennai" OR city="cbe";

SELECT * FROM employees WHERE city IN ("chennai","trichy");

SELECT * FROM employees WHERE salary BETWEEN 35000 AND 50000;

SELECT * FROM employees WHERE name LIKE "G%";

SELECT * FROM employees WHERE name LIKE "%H";

SELECT * FROM employees WHERE NOT city="chennai";

SELECT 
	name AS EMP_NAME,
	department AS DEPT,
	salary AS MONTHLY_SALARY
FROM employees;

SELECT * FROM employees
WHERE city="chennai" AND salary BETWEEN 25000 AND 50000 
ORDER BY salary DESC;

SELECT * FROM employees 
WHERE department='ai&ds' OR
salary>40000;

UPDATE employees
SET salary=salary+5000
WHERE department='ai&ds';

SELECT * FROM employees
ORDER BY salary DESC LIMIT 1;

SELECT * FROM employees
WHERE NOT city='chennai';

SELECT * FROM employees
WHERE  name LIKE '%r%';